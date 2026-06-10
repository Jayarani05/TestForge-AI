"""
Test Execution Service
Executes generated automation tests and captures results.
"""

import subprocess
import logging
import json
import re
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from enum import Enum

logger = logging.getLogger(__name__)


class TestFramework(str, Enum):
    """Supported test frameworks"""
    PYTEST = "pytest"
    NPM = "npm"
    MVN = "mvn"


class ExecutionResult:
    """Represents test execution result"""

    def __init__(
        self,
        framework: str,
        status: str,
        total_tests: int = 0,
        passed_tests: int = 0,
        failed_tests: int = 0,
        skipped_tests: int = 0,
        logs: str = "",
        errors: str = "",
        execution_time: float = 0.0
    ):
        self.framework = framework
        self.status = status
        self.total_tests = total_tests
        self.passed_tests = passed_tests
        self.failed_tests = failed_tests
        self.skipped_tests = skipped_tests
        self.logs = logs
        self.errors = errors
        self.execution_time = execution_time

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "framework": self.framework,
            "status": self.status,
            "total_tests": self.total_tests,
            "passed_tests": self.passed_tests,
            "failed_tests": self.failed_tests,
            "skipped_tests": self.skipped_tests,
            "logs": self.logs[:5000],  # Limit logs to 5000 chars
            "errors": self.errors[:2000],  # Limit errors to 2000 chars
            "execution_time": round(self.execution_time, 2),
            "success": self.status == "success"
        }


class TestExecutor:
    """Executes tests using subprocess and captures results"""

    def __init__(self):
        """Initialize test executor"""
        logger.info("TestExecutor initialized")

    def execute_test_file(
        self,
        file_path: str,
        framework: Optional[str] = None,
        timeout: int = 300
    ) -> ExecutionResult:
        """
        Execute a single test file.

        Args:
            file_path: Path to test file
            framework: Framework to use (auto-detect if None)
            timeout: Timeout in seconds (default 300)

        Returns:
            ExecutionResult with test metrics and logs
        """
        try:
            # Verify file exists
            path = Path(file_path)
            if not path.exists():
                return ExecutionResult(
                    framework="unknown",
                    status="error",
                    errors=f"File not found: {file_path}"
                )

            # Auto-detect framework from file extension
            if not framework:
                framework = self._detect_framework(file_path)

            logger.info(f"Executing test file: {file_path} with framework: {framework}")

            # Execute based on framework
            if framework.lower() == "pytest":
                return self._execute_pytest(file_path, timeout)
            elif framework.lower() == "npm":
                return self._execute_npm(file_path, timeout)
            elif framework.lower() == "mvn":
                return self._execute_mvn(file_path, timeout)
            else:
                return ExecutionResult(
                    framework=framework,
                    status="error",
                    errors=f"Unsupported framework: {framework}"
                )

        except Exception as e:
            logger.error(f"Error executing test file: {str(e)}", exc_info=True)
            return ExecutionResult(
                framework=framework or "unknown",
                status="error",
                errors=str(e)
            )

    def execute_directory(
        self,
        directory: str,
        framework: Optional[str] = None,
        timeout: int = 300
    ) -> ExecutionResult:
        """
        Execute all tests in a directory.

        Args:
            directory: Path to test directory
            framework: Framework to use
            timeout: Timeout in seconds

        Returns:
            Aggregated ExecutionResult
        """
        try:
            dir_path = Path(directory)
            if not dir_path.exists():
                return ExecutionResult(
                    framework=framework or "unknown",
                    status="error",
                    errors=f"Directory not found: {directory}"
                )

            # Auto-detect framework
            if not framework:
                framework = self._detect_framework_from_directory(directory)

            logger.info(f"Executing all tests in: {directory} with framework: {framework}")

            if framework.lower() == "pytest":
                return self._execute_pytest(directory, timeout)
            elif framework.lower() == "npm":
                return self._execute_npm(directory, timeout)
            elif framework.lower() == "mvn":
                return self._execute_mvn(directory, timeout)
            else:
                return ExecutionResult(
                    framework=framework,
                    status="error",
                    errors=f"Unsupported framework: {framework}"
                )

        except Exception as e:
            logger.error(f"Error executing directory: {str(e)}")
            return ExecutionResult(
                framework=framework or "unknown",
                status="error",
                errors=str(e)
            )

    def _detect_framework(self, file_path: str) -> str:
        """Detect framework from file extension"""
        path = Path(file_path)
        ext = path.suffix.lower()

        if ext == ".py":
            return "pytest"
        elif ext in [".js", ".ts"]:
            return "npm"
        elif ext == ".java":
            return "mvn"
        else:
            return "unknown"

    def _detect_framework_from_directory(self, directory: str) -> str:
        """Detect framework from directory contents"""
        dir_path = Path(directory)

        # Check for pytest files
        if list(dir_path.glob("test_*.py")) or list(dir_path.glob("*_test.py")):
            return "pytest"

        # Check for npm test files
        if list(dir_path.glob("*.test.js")) or list(dir_path.glob("*.spec.js")):
            return "npm"

        # Check for maven files
        if (dir_path / "pom.xml").exists():
            return "mvn"

        return "unknown"

    def _execute_pytest(
        self,
        path: str,
        timeout: int
    ) -> ExecutionResult:
        """Execute pytest framework tests"""
        try:
            import time
            start_time = time.time()

            # Build pytest command
            cmd = [
                "pytest",
                path,
                "-v",  # Verbose output
                "--tb=short",  # Short traceback format
                "-ra",  # Show summary of all test outcomes
                "--json-report",  # JSON report (if available)
                "--json-report-file=/tmp/report.json"  # Report file
            ]

            # Run pytest
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            execution_time = time.time() - start_time

            # Parse output
            stdout = result.stdout
            stderr = result.stderr
            return_code = result.returncode

            # Extract metrics from pytest output
            total, passed, failed, skipped = self._parse_pytest_output(stdout)

            status = "success" if return_code == 0 else "failed"

            return ExecutionResult(
                framework="pytest",
                status=status,
                total_tests=total,
                passed_tests=passed,
                failed_tests=failed,
                skipped_tests=skipped,
                logs=stdout,
                errors=stderr,
                execution_time=execution_time
            )

        except subprocess.TimeoutExpired:
            logger.error(f"Pytest execution timed out after {timeout}s")
            return ExecutionResult(
                framework="pytest",
                status="timeout",
                errors=f"Test execution timed out after {timeout} seconds"
            )
        except FileNotFoundError:
            logger.error("pytest not found. Install with: pip install pytest")
            return ExecutionResult(
                framework="pytest",
                status="error",
                errors="pytest is not installed. Install with: pip install pytest"
            )
        except Exception as e:
            logger.error(f"Error executing pytest: {str(e)}")
            return ExecutionResult(
                framework="pytest",
                status="error",
                errors=str(e)
            )

    def _execute_npm(
        self,
        path: str,
        timeout: int
    ) -> ExecutionResult:
        """Execute npm test framework"""
        try:
            import time
            start_time = time.time()

            # Build npm command
            cmd = ["npm", "test", "--", path]

            # Run npm test
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=Path(path).parent if Path(path).is_file() else path
            )

            execution_time = time.time() - start_time

            stdout = result.stdout
            stderr = result.stderr
            return_code = result.returncode

            # Extract metrics from npm output
            total, passed, failed = self._parse_npm_output(stdout)

            status = "success" if return_code == 0 else "failed"

            return ExecutionResult(
                framework="npm",
                status=status,
                total_tests=total,
                passed_tests=passed,
                failed_tests=failed,
                logs=stdout,
                errors=stderr,
                execution_time=execution_time
            )

        except subprocess.TimeoutExpired:
            logger.error(f"npm test execution timed out after {timeout}s")
            return ExecutionResult(
                framework="npm",
                status="timeout",
                errors=f"Test execution timed out after {timeout} seconds"
            )
        except FileNotFoundError:
            logger.error("npm not found")
            return ExecutionResult(
                framework="npm",
                status="error",
                errors="npm is not installed or not in PATH"
            )
        except Exception as e:
            logger.error(f"Error executing npm test: {str(e)}")
            return ExecutionResult(
                framework="npm",
                status="error",
                errors=str(e)
            )

    def _execute_mvn(
        self,
        path: str,
        timeout: int
    ) -> ExecutionResult:
        """Execute maven test framework"""
        try:
            import time
            start_time = time.time()

            # Determine working directory
            work_dir = path if Path(path).is_dir() else Path(path).parent

            # Build maven command
            cmd = [
                "mvn",
                "test",
                "-f", str(Path(work_dir) / "pom.xml"),
                "-DsurefireReportsDirectory=target/surefire-reports"
            ]

            # Run mvn test
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(work_dir)
            )

            execution_time = time.time() - start_time

            stdout = result.stdout
            stderr = result.stderr
            return_code = result.returncode

            # Extract metrics from maven output
            total, passed, failed = self._parse_mvn_output(stdout)

            status = "success" if return_code == 0 else "failed"

            return ExecutionResult(
                framework="mvn",
                status=status,
                total_tests=total,
                passed_tests=passed,
                failed_tests=failed,
                logs=stdout,
                errors=stderr,
                execution_time=execution_time
            )

        except subprocess.TimeoutExpired:
            logger.error(f"Maven test execution timed out after {timeout}s")
            return ExecutionResult(
                framework="mvn",
                status="timeout",
                errors=f"Test execution timed out after {timeout} seconds"
            )
        except FileNotFoundError:
            logger.error("mvn not found")
            return ExecutionResult(
                framework="mvn",
                status="error",
                errors="Maven (mvn) is not installed or not in PATH"
            )
        except Exception as e:
            logger.error(f"Error executing mvn test: {str(e)}")
            return ExecutionResult(
                framework="mvn",
                status="error",
                errors=str(e)
            )

    def _parse_pytest_output(self, output: str) -> Tuple[int, int, int, int]:
        """Parse pytest output to extract test counts"""
        try:
            total = 0
            passed = 0
            failed = 0
            skipped = 0

            # Look for summary line: "5 passed in 0.50s"
            # Pattern: X passed, Y failed, Z skipped
            summary_pattern = r"(\d+)\s+passed"
            match = re.search(summary_pattern, output)
            if match:
                passed = int(match.group(1))

            summary_pattern = r"(\d+)\s+failed"
            match = re.search(summary_pattern, output)
            if match:
                failed = int(match.group(1))

            summary_pattern = r"(\d+)\s+skipped"
            match = re.search(summary_pattern, output)
            if match:
                skipped = int(match.group(1))

            total = passed + failed + skipped

            return total, passed, failed, skipped

        except Exception as e:
            logger.warning(f"Error parsing pytest output: {str(e)}")
            return 0, 0, 0, 0

    def _parse_npm_output(self, output: str) -> Tuple[int, int, int]:
        """Parse npm test output to extract test counts"""
        try:
            total = 0
            passed = 0
            failed = 0

            # Look for patterns like "5 passed" or "1 failed"
            passed_pattern = r"(\d+)\s+passed"
            match = re.search(passed_pattern, output)
            if match:
                passed = int(match.group(1))

            failed_pattern = r"(\d+)\s+failed"
            match = re.search(failed_pattern, output)
            if match:
                failed = int(match.group(1))

            total = passed + failed

            return total, passed, failed

        except Exception as e:
            logger.warning(f"Error parsing npm output: {str(e)}")
            return 0, 0, 0

    def _parse_mvn_output(self, output: str) -> Tuple[int, int, int]:
        """Parse maven output to extract test counts"""
        try:
            total = 0
            passed = 0
            failed = 0

            # Look for: "Tests run: 5, Failures: 0, Errors: 0"
            pattern = r"Tests run:\s*(\d+),.*?Failures:\s*(\d+),.*?Errors:\s*(\d+)"
            match = re.search(pattern, output)

            if match:
                total = int(match.group(1))
                failed = int(match.group(2)) + int(match.group(3))
                passed = total - failed

            return total, passed, failed

        except Exception as e:
            logger.warning(f"Error parsing maven output: {str(e)}")
            return 0, 0, 0
