import os
import re
import json
from pathlib import Path


IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', '.venv', 'env', 'dist', 'build', '.pytest_cache', 'coverage', '.next', 'out'}
IGNORE_FILES = {'.gitignore', '.DS_Store', '.env', 'Thumbs.db'}
SOURCE_FILE_EXTENSIONS = {'.py', '.java', '.js', '.jsx', '.ts', '.tsx', '.go', '.rs', '.php', '.rb', '.c', '.cpp', '.cs', '.h', '.hpp'}


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


def extract_dependencies(repo_path: str) -> list:
    """Extract dependencies from various configuration files."""
    dependencies = []
    
    # Python: requirements.txt
    req_file = os.path.join(repo_path, 'requirements.txt')
    if os.path.exists(req_file):
        try:
            with open(req_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        pkg = re.split(r'[=<>!]', line)[0].strip()
                        if pkg and pkg not in dependencies:
                            dependencies.append(pkg)
        except:
            pass
    
    # JavaScript: package.json
    package_json = os.path.join(repo_path, 'package.json')
    if os.path.exists(package_json):
        try:
            with open(package_json, 'r') as f:
                data = json.load(f)
                for deps_key in ['dependencies', 'devDependencies', 'peerDependencies']:
                    if deps_key in data:
                        for pkg in data[deps_key].keys():
                            if pkg not in dependencies:
                                dependencies.append(pkg)
        except:
            pass
    
    # Java: pom.xml
    pom_file = os.path.join(repo_path, 'pom.xml')
    if os.path.exists(pom_file):
        try:
            with open(pom_file, 'r') as f:
                content = f.read()
                artifacts = re.findall(r'<artifactId>([^<]+)</artifactId>', content)
                for artifact in artifacts[:20]:
                    if artifact not in dependencies and artifact != 'maven-plugins':
                        dependencies.append(artifact)
        except:
            pass
    
    return dependencies[:50]


def extract_api_endpoints(repo_path: str, language: str) -> list:
    """Extract API endpoints/routes based on language."""
    endpoints = []
    
    if language == "Python":
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                if file.endswith('.py'):
                    try:
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            routes = re.findall(r'@(?:app|router)\.(?:get|post|put|delete|patch|head|options)\s*\(\s*["\']([^"\']+)["\']', content)
                            for route in routes:
                                if route not in endpoints:
                                    endpoints.append(route)
                    except:
                        pass
    
    elif language == "Java":
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                if file.endswith('.java'):
                    try:
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            class_mappings = re.findall(r'@RequestMapping\s*\(\s*["\']?([^"\')\s]+)', content)
                            method_mappings = re.findall(r'@(?:GetMapping|PostMapping|PutMapping|DeleteMapping)\s*\(\s*["\']([^"\']+)', content)
                            for mapping in class_mappings + method_mappings:
                                if mapping and mapping not in endpoints:
                                    endpoints.append(mapping)
                    except:
                        pass
    
    elif language == "JavaScript":
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                if file.endswith(('.js', '.jsx', '.ts', '.tsx')):
                    try:
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            routes = re.findall(r'(?:app|router)\.(?:get|post|put|delete|patch)\s*\(\s*["\']([^"\']+)["\']', content)
                            for route in routes:
                                if route not in endpoints:
                                    endpoints.append(route)
                    except:
                        pass
    
    return endpoints[:50]


def extract_classes(repo_path: str, language: str) -> list:
    """Extract class definitions based on language."""
    classes = []
    
    if language == "Python":
        pattern = r'class\s+(\w+)\s*(?:\(|:|$)'
    elif language == "Java":
        pattern = r'(?:public|private|protected)?\s*class\s+(\w+)(?:\s+extends|\s+implements|\s*\{|$)'
    elif language == "JavaScript":
        pattern = r'class\s+(\w+)(?:\s+extends|\s*\{|$)'
    else:
        return classes
    
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if (language == "Python" and file.endswith('.py')) or \
               (language == "Java" and file.endswith('.java')) or \
               (language == "JavaScript" and file.endswith(('.js', '.jsx', '.ts', '.tsx'))):
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = re.findall(pattern, content)
                        for class_name in matches:
                            if class_name not in classes and class_name not in ['React', 'Component']:
                                classes.append(class_name)
                except:
                    pass
    
    return classes[:50]


def extract_functions(repo_path: str, language: str) -> list:
    """Extract function/method definitions based on language."""
    functions = []
    
    if language == "Python":
        pattern = r'def\s+(\w+)\s*\('
    elif language == "Java":
        pattern = r'(?:public|private|protected)?\s*(?:static)?\s*(?:void|String|int|boolean|List|Map|Object|\w+)\s+(\w+)\s*\('
    elif language == "JavaScript":
        pattern = r'(?:function\s+(\w+)\s*\(|const\s+(\w+)\s*=|(?:async\s+)?(\w+)\s*[=:])'
    else:
        return functions
    
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if (language == "Python" and file.endswith('.py')) or \
               (language == "Java" and file.endswith('.java')) or \
               (language == "JavaScript" and file.endswith(('.js', '.jsx', '.ts', '.tsx'))):
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = re.findall(pattern, content)
                        for func_match in matches:
                            func_name = func_match[0] if isinstance(func_match, tuple) else func_match
                            if not func_name and isinstance(func_match, tuple) and len(func_match) > 1:
                                func_name = func_match[1]
                            if not func_name and isinstance(func_match, tuple) and len(func_match) > 2:
                                func_name = func_match[2]
                            if func_name and func_name not in functions and func_name and func_name[0].islower():
                                functions.append(func_name)
                except:
                    pass
    
    return functions[:50]


def extract_source_files(repo_path: str) -> list:
    """Extract important source files based on priority."""
    source_files = []
    priority_files = {
        'main.py': 10, 'app.py': 10, 'settings.py': 9, '__init__.py': 8, 'manage.py': 9,
        'index.js': 10, 'index.jsx': 10, 'App.js': 10, 'App.jsx': 10, 'main.jsx': 10,
        'pom.xml': 8, 'build.gradle': 8, 'package.json': 8, 'requirements.txt': 8,
    }
    
    priority_dirs = {
        'src': 10, 'app': 10, 'controllers': 9, 'services': 9, 'components': 9, 'pages': 9, 'models': 8, 'utils': 8, 'api': 9,
    }
    
    file_scores = {}
    
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        dir_score = 0
        for dir_name in priority_dirs:
            if dir_name in root.lower():
                dir_score = priority_dirs[dir_name]
                break
        
        for file in files:
            if file.endswith(tuple(SOURCE_FILE_EXTENSIONS)):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, repo_path)
                score = dir_score
                if file in priority_files:
                    score = max(score, priority_files[file])
                if any(keyword in rel_path.lower() for keyword in ['api', 'route', 'controller', 'endpoint']):
                    score += 2
                file_scores[rel_path] = score
    
    sorted_files = sorted(file_scores.items(), key=lambda x: (-x[1], x[0]))
    source_files = [file[0] for file in sorted_files[:40]]
    return source_files


def analyze_repository(repo_path: str) -> dict:
    """
    Analyze a cloned repository and return comprehensive analysis results.
    
    Args:
        repo_path: Path to the cloned repository
        
    Returns:
        Dictionary containing detailed analysis results with source files, endpoints, classes, functions, and dependencies
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
    
    # Extract deeper project understanding
    source_files = extract_source_files(repo_path)
    api_endpoints = extract_api_endpoints(repo_path, language)
    classes = extract_classes(repo_path, language)
    functions = extract_functions(repo_path, language)
    dependencies = extract_dependencies(repo_path)
    
    result = {
        "project_name": project_name,
        "language": language,
        "framework": framework,
        "total_files": len(all_files),
        "structure": structure[:50],
        "source_files": source_files,
        "api_endpoints": api_endpoints,
        "classes": classes,
        "functions": functions,
        "dependencies": dependencies,
        "status": "success"
    }
    
    return result