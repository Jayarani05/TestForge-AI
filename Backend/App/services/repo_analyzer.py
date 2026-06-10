import os


def detect_language(files):

    extensions = {
        ".py": "Python",
        ".java": "Java",
        ".js": "JavaScript",
        ".jsx": "React",
        ".ts": "TypeScript"
    }

    count = {}

    for file in files:
        ext = os.path.splitext(file)[1]

        if ext in extensions:
            lang = extensions[ext]
            count[lang] = count.get(lang, 0) + 1

    if not count:
        return "Unknown"

    return max(count, key=count.get)



def detect_framework(files):

    filenames = [
        os.path.basename(file)
        for file in files
    ]

    if "package.json" in filenames:
        return "React / Node"

    if "requirements.txt" in filenames:
        return "Python"

    if "pom.xml" in filenames:
        return "Spring Boot"

    return "Unknown"



def analyze_repository(repo_path):

    all_files = []

    for root, dirs, files in os.walk(repo_path):

        if ".git" in root:
            continue

        for file in files:
            all_files.append(
                os.path.join(root, file)
            )


    result = {

        "total_files": len(all_files),

        "language": detect_language(
            all_files
        ),

        "framework": detect_framework(
            all_files
        ),

        "sample_files": [
            os.path.basename(file)
            for file in all_files[:20]
        ]

    }

    return result