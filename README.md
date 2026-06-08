# 🚀 TestForge AI

### Agentic AI Powered QA Automation Platform

TestForge AI is an intelligent QA automation platform that leverages Agentic AI and Multiple Large Language Models (LLMs) to automate the software testing lifecycle. The platform transforms requirements into optimized test cases, automation scripts, bug analysis reports, CI/CD pipelines, and actionable QA insights.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-purple)
![LLM](https://img.shields.io/badge/MultiLLM-Gemini%20%7C%20Llama%20%7C%20DeepSeek-orange)

---

# 📌 Project Overview

TestForge AI automates key QA engineering activities through a collection of specialized AI agents. By combining requirement understanding, multi-model reasoning, automated test generation, execution analysis, and bug diagnostics, the platform helps QA teams improve efficiency, coverage, and software quality.

---

# 🎯 Problem Statement

Software testing involves significant manual effort in:

* Understanding requirements
* Designing test cases
* Creating automation scripts
* Investigating failures
* Maintaining automation frameworks
* Configuring CI/CD pipelines

These activities are often time-consuming and repetitive.

TestForge AI addresses these challenges using Agentic AI workflows that automate and optimize the complete testing process.

---

# ✨ Features

| Feature                    | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| 🤖 Requirement Agent       | Understands user stories and testing scope            |
| 🧠 Multi-LLM Engine        | Generates responses using Gemini, Llama, and DeepSeek |
| ⚖️ Judge Agent             | Evaluates and selects the best AI response            |
| 📝 Test Case Generator     | Creates positive, negative, and edge-case scenarios   |
| 💻 Automation Generator    | Generates automation scripts                          |
| ▶️ Test Execution Agent    | Executes generated automation tests                   |
| 🐞 AI Bug Analyzer         | Performs root cause analysis on failures              |
| 🔧 Self-Healing Agent      | Repairs broken automation scripts and locators        |
| 📂 Repository Intelligence | Analyzes repositories and project structures          |
| 🚀 CI/CD Generator         | Creates GitHub Actions and deployment pipelines       |
| 📊 Dashboard Analytics     | Provides QA insights and project metrics              |
| 📄 Export Center           | Exports reports and generated artifacts               |
| 🔐 Authentication          | Secure JWT-based authentication                       |

---

# 🤖 AI Agents

## Requirement Agent

Analyzes:

* User stories
* Business requirements
* Testing scope
* Potential risks

---

## Multi-LLM Orchestrator

Connected Models:

* Google Gemini
* Llama
* DeepSeek

Each model independently generates responses for improved coverage and quality.

---

## Judge Agent

Evaluates outputs based on:

* Accuracy
* Completeness
* Coverage
* Quality

Selects the most effective response.

---

## Test Generation Agent

Generates:

* Positive test cases
* Negative test cases
* Boundary scenarios
* Edge cases
* Security test scenarios

---

## Automation Generator

Creates automation scripts using:

* Python
* Java
* JavaScript
* Selenium
* Playwright
* JUnit

---

## Test Execution Agent

Handles:

* Script execution
* Test results
* Logs collection
* Execution tracking

---

## AI Bug Analyzer Agent

Provides:

* Root cause analysis
* Failure explanations
* Severity assessment
* Recommended fixes

---

## Self-Healing Agent

Automatically resolves:

* Broken Selenium locators
* DOM changes
* Automation failures

---

## Repository Intelligence Agent

Analyzes:

* Project architecture
* Technology stack
* Code organization
* Improvement opportunities

---

## CI/CD Agent

Generates:

* GitHub Actions workflows
* QA pipelines
* Automation setup configurations

---

# 🏗️ System Architecture

```text
                    User Requirement

                           │
                           ▼

                 Requirement Agent

                           │
                           ▼

               Multi-LLM Orchestrator

           Gemini     Llama     DeepSeek
                \        |        /

                    Judge Agent

                           │
                           ▼

                Optimized QA Response

                           │
 ─────────────────────────────────────────────

     Test       Execution      Bug       DevOps
    Agent         Agent      Analyzer    Agent

                           │
                           ▼

                 QA Automation Output
```

---

# ⚙️ Technology Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication

### Frontend

* React JS
* Tailwind CSS
* Axios

### AI & LLMs

* Google Gemini
* Llama
* DeepSeek
* Agentic AI Architecture

### Testing & Automation

* Selenium
* Pytest

---

# 📂 Project Structure

```text
TestForge-AI/

│
├── Backend/
│   │
│   └── app/
│       ├── agents/
│       ├── api/
│       ├── database/
│       ├── llm_services/
│       ├── schemas/
│       ├── security/
│       └── main.py
│
├── Frontend/
│   │
│   └── src/
│       ├── pages/
│       ├── components/
│       ├── services/
│       └── assets/
│
├── Documents/
│   ├── AI_USAGE.md
│   ├── DEMO.md
│   └── TEST_CASES.md
│
├── Output/
│   ├── reports/
│   ├── exports/
│   └── screenshots/
│
├── README.md
│
└── .gitignore
```

---

# 🔄 Workflow

1. User submits a requirement or user story.
2. Requirement Agent analyzes the request.
3. Gemini, Llama, and DeepSeek generate independent responses.
4. Judge Agent evaluates and selects the best output.
5. Test cases and automation scripts are generated.
6. Execution Agent runs generated tests.
7. Bug Analyzer investigates failures.
8. Reports and analytics are generated.
9. Results are exported for QA teams.

---

# 🚀 Installation

## Backend Setup

```bash
cd Backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd Frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# ▶️ Run Tests

```bash
pytest
```

---

# 🎬 Demo Video

### Project Demonstration

Demo Folder:

https://drive.google.com/drive/folders/1MMhRRGd6zoAp46JXAaSimzBJfuoONZvg

---

# 📚 Documentation

Available in:

```text
https://github.com/Jayarani05/TestForge-AI/tree/main/Documents
```

Includes:

* AI Usage Documentation
* Demo Guide
* Test Cases
* Project Reports

---

# 🔒 Security

* JWT Authentication
* Protected API Endpoints
* Secure User Access
* Environment Variable Configuration
* Role-Based Access Control Ready

---

# 🔮 Future Enhancements

* Cloud Deployment
* Real Browser Automation Execution
* Advanced QA Analytics
* Enterprise Test Management
* Additional LLM Integrations
* Team Collaboration Features
* Enhanced Self-Healing Mechanisms

---

# 👥 Team Members      

Jayarani M       
Harshini T     
Hemadharshini M
Hrithickram R   

---

# 📖 About

TestForge AI demonstrates how Agentic AI and Multi-LLM collaboration can transform traditional software testing by automating requirement analysis, test generation, execution, bug analysis, repository intelligence, and DevOps workflows—enabling faster delivery and higher software quality.
