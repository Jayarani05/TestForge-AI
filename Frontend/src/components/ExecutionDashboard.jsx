import { useState } from "react";
import { runTests } from "../api/workflowApi";
import Loader from "./Loader";
import "./ExecutionDashboard.css";

export default function ExecutionDashboard({
  generatedCode,
  onExecutionComplete,
  onLoading,
}) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [executionResult, setExecutionResult] = useState(null);
  const [logsExpanded, setLogsExpanded] = useState(false);

  const getTestFilePath = () => {
    if (generatedCode?.file_info?.saved_file) {
      return generatedCode.file_info.saved_file;
    }
    if (generatedCode?.generated_files?.[0]?.file_path) {
      return generatedCode.generated_files[0].file_path;
    }
    return null;
  };

  const handleRunTests = async () => {
    const filePath = getTestFilePath();

    if (!filePath) {
      setError("No generated test file found. Please generate automation code first.");
      return;
    }

    setLoading(true);
    setError("");
    onLoading?.(true);

    try {
      const result = await runTests(
        filePath,
        generatedCode?.framework,
        300
      );

      if (result.status === "error") {
        setError(result.error || "Failed to run tests");
        return;
      }

      setExecutionResult(result);
      onExecutionComplete?.(result);
    } catch (err) {
      setError(err.error || err.message || "Failed to run tests");
    } finally {
      setLoading(false);
      onLoading?.(false);
    }
  };

  const getSuccessRate = () => {
    if (!executionResult || executionResult.total_tests === 0) return 0;
    return (
      (executionResult.passed_tests / executionResult.total_tests) * 100
    ).toFixed(1);
  };

  return (
    <div className="execution-dashboard">
      <div className="dashboard-card">
        <h2>Test Execution Dashboard</h2>
        <p className="subtitle">Execute generated automation tests and monitor results</p>

        {!generatedCode && (
          <div className="warning-message">
            ⚠️ Please generate automation code first
          </div>
        )}

        <div className="execution-info">
          <span className="info-label">Test File:</span>
          <span className="info-value">
            {getTestFilePath() || "No file path"}
          </span>
          <span className="info-label">Framework:</span>
          <span className="info-value">
            {generatedCode?.framework || "Unknown"}
          </span>
        </div>

        {error && <span className="error-message">{error}</span>}

        <button
          onClick={handleRunTests}
          disabled={loading || !generatedCode}
          className="run-btn"
        >
          {loading ? (
            <>
              <Loader size={16} style={{ marginRight: "8px" }} />
              Running Tests...
            </>
          ) : (
            "Run Tests"
          )}
        </button>

        {executionResult && (
          <div className="execution-results">
            <div className="results-summary">
              <h3>Test Results</h3>

              <div className="metrics-grid">
                <div className={`metric-card ${executionResult.status}`}>
                  <span className="metric-label">Status</span>
                  <span
                    className={`metric-value status-${executionResult.status}`}
                  >
                    {executionResult.status.toUpperCase()}
                  </span>
                </div>

                <div className="metric-card">
                  <span className="metric-label">Total Tests</span>
                  <span className="metric-value">
                    {executionResult.total_tests}
                  </span>
                </div>

                <div className="metric-card passed">
                  <span className="metric-label">Passed</span>
                  <span className="metric-value">
                    {executionResult.passed_tests}
                  </span>
                </div>

                <div className="metric-card failed">
                  <span className="metric-label">Failed</span>
                  <span className="metric-value">
                    {executionResult.failed_tests}
                  </span>
                </div>

                {executionResult.skipped_tests > 0 && (
                  <div className="metric-card skipped">
                    <span className="metric-label">Skipped</span>
                    <span className="metric-value">
                      {executionResult.skipped_tests}
                    </span>
                  </div>
                )}

                <div className="metric-card">
                  <span className="metric-label">Success Rate</span>
                  <span className="metric-value">
                    {getSuccessRate()}%
                  </span>
                </div>

                <div className="metric-card">
                  <span className="metric-label">Execution Time</span>
                  <span className="metric-value">
                    {executionResult.execution_time}s
                  </span>
                </div>
              </div>

              {executionResult.total_tests > 0 && (
                <div className="progress-bar-container">
                  <div className="progress-bar">
                    <div
                      className="progress-passed"
                      style={{
                        width: `${(executionResult.passed_tests / executionResult.total_tests) * 100}%`,
                      }}
                    />
                    <div
                      className="progress-failed"
                      style={{
                        width: `${(executionResult.failed_tests / executionResult.total_tests) * 100}%`,
                      }}
                    />
                    {executionResult.skipped_tests > 0 && (
                      <div
                        className="progress-skipped"
                        style={{
                          width: `${(executionResult.skipped_tests / executionResult.total_tests) * 100}%`,
                        }}
                      />
                    )}
                  </div>
                </div>
              )}
            </div>

            {executionResult.logs && (
              <div className="logs-section">
                <button
                  className="logs-toggle"
                  onClick={() => setLogsExpanded(!logsExpanded)}
                >
                  {logsExpanded ? "▼" : "▶"} Execution Logs ({executionResult.logs.length} chars)
                </button>

                {logsExpanded && (
                  <div className="logs-viewer">
                    <pre>{executionResult.logs}</pre>
                  </div>
                )}
              </div>
            )}

            {executionResult.errors && (
              <div className="errors-section">
                <h4>Errors</h4>
                <div className="errors-viewer">
                  <pre>{executionResult.errors}</pre>
                </div>
              </div>
            )}

            <div className="result-footer">
              {executionResult.status === "success" ? (
                <p className="success-message">
                  ✅ All tests passed! Your automation suite is working correctly.
                </p>
              ) : executionResult.status === "failed" ? (
                <p className="failure-message">
                  ❌ Some tests failed. Check the logs above for details.
                </p>
              ) : (
                <p className="warning-message">
                  ⚠️ Test execution completed with status: {executionResult.status}
                </p>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
