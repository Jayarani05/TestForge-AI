import os
from pathlib import Path


IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', '.venv', 'env', 'dist', 'build', '.pytest_cache'}
IGNORE_FILES = {'.gitignore', '.DS_Store', '.env', 'Thumbs.db'}


def get_project_name(repo_path: str) -> str:
    """Extract project name from repository path or by detecting package name."""
    
    # Try to get from directory name
    project_name = os.path.basename(repo_path.rstrip('/\\'))
    
    # Try to get from setup.py or pyproject.toml
    setup_py = os.path.join(repo_path, 'setup.py')
    if os.path.exists(setup_py):
        try:
            with open(setup_py, 'r') as f:
                content = f.read()
                if 'name=' in content:
                    start = content.find('name=') + 5
                    end = content.find(',', start)
                    if end == -1:
                        end = content.find(')', start)
                    name = content[start:end].strip().strip('\'"')
                    if name:
                        project_name = name
        except:
            pass
    
    # Try package.json
    package_json = os.path.join(repo_path, 'package.json')
    if os.path.exists(package_json):
        try:
            import json
            with open(package_json, 'r') as f:
                data = json.load(f)
                if 'name' in data:
                    project_name = data['name']
        except:
            pass
    
    return project_name


def detect_language(files: list) -> str:
    """Detect primary programming language based on file extensions."""
    
    extensions = {
        ".py": "Python",
        ".java": "Java",
        ".js": "JavaScript",
        ".jsx": "JavaScript",
        ".ts": "TypeScript",
        ".tsx": "TypeScript",
        ".go": "Go",
        ".rs": "Rust",
        ".php": "PHP",
        ".rb": "Ruby",
        ".c": "C",
        ".cpp": "C++",
        ".cs": "C#"
    }
    
    count = {}
    
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        
        if ext in extensions:
            lang = extensions[ext]
            count[lang] = count.get(lang, 0) + 1
    
    if not count:
        return "Unknown"
    
    return max(count, key=count.get)


def detect_framework(files: list, repo_path: str) -> str:
    """Detect framework based on dependency files and imports."""
    
    filenames = {os.path.basename(file) for file in files}
    
    # Check Python frameworks
    if "requirements.txt" in filenames or "setup.py" in filenames or "pyproject.toml" in filenames:
        # Read requirements.txt to detect specific framework
        req_file = os.path.join(repo_path, 'requirements.txt')
        if os.path.exists(req_file):
            try:
                with open(req_file, 'r') as f:
                    content = f.read().lower()
                    if 'fastapi' in content:
                        return "FastAPI"
                    elif 'django' in content:
                        return "Django"
                    elif 'flask' in content:
                        return "Flask"
                    elif 'pytest' in content:
                        return "Python (Testing)"
            except:
                pass
        
        # Check pyproject.toml
        pyproject_file = os.path.join(repo_path, 'pyproject.toml')
        if os.path.exists(pyproject_file):
            try:
                with open(pyproject_file, 'r') as f:
                    content = f.read().lower()
                    if 'fastapi' in content:
                        return "FastAPI"
                    elif 'django' in content:
                        return "Django"
                    elif 'flask' in content:
                        return "Flask"
            except:
                pass
        
        return "Python"
    
    # Check JavaScript/Node.js frameworks
    if "package.json" in filenames:
        package_json = os.path.join(repo_path, 'package.json')
        if os.path.exists(package_json):
            try:
                import json
                with open(package_json, 'r') as f:
                    data = json.load(f)
                    deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                    
                    if 'react' in deps:
                        return "React"
                    elif 'vue' in deps:
                        return "Vue.js"
                    elif 'angular' in deps:
                        return "Angular"
                    elif 'express' in deps:
                        return "Express.js"
                    elif 'next' in deps:
                        return "Next.js"
            except:
                pass
        
        return "Node.js"
    
    # Check Java frameworks
    if "pom.xml" in filenames:
        pom_file = os.path.join(repo_path, 'pom.xml')
        if os.path.exists(pom_file):
            try:
                with open(pom_file, 'r') as f:
                    content = f.read().lower()
                    if 'spring-boot' in content:
                        return "Spring Boot"
                    elif 'spring' in content:
                        return "Spring"
            except:
                pass
        return "Java"
    
    if "build.gradle" in filenames:
        gradle_file = os.path.join(repo_path, 'build.gradle')
        if os.path.exists(gradle_file):
            try:
                with open(gradle_file, 'r') as f:
                    content = f.read().lower()
                    if 'spring-boot' in content:
                        return "Spring Boot"
                    elif 'spring' in content:
                        return "Spring"
            except:
                pass
        return "Gradle"
    
    return "Unknown"


def build_folder_structure(repo_path: str, max_depth: int = 3) -> list:
    """Build folder structure for the repository."""
    
    structure = []
    
    def traverse(path: str, prefix: str = "", depth: int = 0):
        """Recursively traverse directory structure."""
        
        if depth > max_depth:
            return
        
        try:
            items = sorted(os.listdir(path))
        except PermissionError:
            return
        
        dirs = []
        files = []
        
        for item in items:
            # Skip ignored directories and files
            if item in IGNORE_DIRS or item in IGNORE_FILES:
                continue
            
            item_path = os.path.join(path, item)
            
            if os.path.isdir(item_path):
                dirs.append(item)
            elif os.path.isfile(item_path):
                files.append(item)
        
        # Add directories
        for i, dir_name in enumerate(dirs):
            is_last_dir = (i == len(dirs) - 1) and len(files) == 0
            structure.append({
                "name": dir_name,
                "type": "folder",
                "level": depth
            })
            
            dir_path = os.path.join(path, dir_name)
            traverse(dir_path, prefix, depth + 1)
        
        # Add files (limited to 10 per folder for readability)
        for i, file_name in enumerate(files[:10]):
            structure.append({
                "name": file_name,
                "type": "file",
                "level": depth
            })
        
        if len(files) > 10:
            structure.append({
                "name": f"... and {len(files) - 10} more files",
                "type": "more",
                "level": depth
            })
    
    traverse(repo_path)
    return structure


def analyze_repository(repo_path: str) -> dict:
    """
    Analyze a cloned repository and return analysis results.
    
    Args:
        repo_path: Path to the cloned repository
        
    Returns:
        Dictionary containing analysis results
    """
    
    if not os.path.exists(repo_path):
        raise ValueError(f"Repository path does not exist: {repo_path}")
    
    # Collect all files
    all_files = []
    
    for root, dirs, files in os.walk(repo_path):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if file not in IGNORE_FILES:
                all_files.append(os.path.join(root, file))
    
    # Get project name
    project_name = get_project_name(repo_path)
    
    # Detect language and framework
    language = detect_language(all_files)
    framework = detect_framework(all_files, repo_path)
    
    # Build folder structure
    structure = build_folder_structure(repo_path)
    
    result = {
        "project_name": project_name,
        "language": language,
        "framework": framework,
        "total_files": len(all_files),
        "structure": structure[:50],  # Limit structure output to first 50 items
        "status": "success"
    }
    
    return result