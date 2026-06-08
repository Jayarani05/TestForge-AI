# TestForge AI

## Project Overview

TestForge AI is an Agentic AI-powered QA Automation Platform that transforms software requirements into optimized test cases, automation scripts, bug analysis reports, CI/CD pipelines, and QA insights using multiple AI agents.

The platform leverages multiple Large Language Models (LLMs) and intelligent agent workflows to automate key stages of the Software Testing Lifecycle (STLC).

---

## Problem Statement

Manual test design, execution, bug analysis, and automation development require significant effort and time from QA teams.

TestForge AI automates these activities using Agentic AI, helping teams improve productivity, testing coverage, and software quality.

---

## Features

* AI-Powered Test Case Generation
* Requirement Analysis Agent
* Multi-LLM Response Generation
* Judge Agent for Response Evaluation
* Automation Script Generation
* Test Execution Engine
* AI Bug Analyzer
* Self-Healing Test Automation
* Repository Analysis
* CI/CD Pipeline Generation
* Project Context Awareness
* QA Report Export
* Dashboard Analytics
* JWT Authentication

---

## AI Techniques Used

* Agentic AI Architecture
* Multi-Agent Collaboration
* Prompt Engineering
* Chain-of-Thought Reasoning
* Multi-LLM Orchestration
* AI-Based Decision Making
* Automated Code Generation
* Root Cause Analysis
* Self-Healing Automation

---

## Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication

### Frontend

* React JS
* Tailwind CSS
* Axios

### AI Models

* Google Gemini
* Llama
* DeepSeek

### Testing & Automation

* Selenium
* Pytest

---

## Project Structure

```text
TestForge-AI/

Backend/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── database/
│   ├── llm_services/
│   ├── security/
│   └── schemas/
│
Frontend/
│
├── src/
│   ├── pages/
│   ├── components/
│   └── services/
│
Documents/
│
├── AI_USAGE.md
├── DEMO.md
└── TEST_CASES.md
│
Output/
│
├── reports/
├── exports/
└── screenshots/
│
README.md
```

---

## Workflow

1. User submits a requirement or user story.
2. Requirement Agent analyzes the input.
3. Gemini, Llama, and DeepSeek generate independent responses.
4. Judge Agent evaluates and selects the best output.
5. Test cases and automation scripts are generated.
6. Execution Agent runs generated tests.
7. Bug Analyzer identifies root causes and recommendations.
8. Reports and analytics are generated for users.

---

## Installation

### Backend Setup

```bash
cd Backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Frontend Setup

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

## Demo Videos

### Project Demonstration

Demo Video:

https://drive.google.com/drive/folders/1MMhRRGd6zoAp46JXAaSimzBJfuoONZvg

---

## Future Enhancements

* Cloud Deployment
* Advanced Test Analytics
* Additional LLM Integrations
* Enterprise QA Management
* Real-Time Collaboration
* Browser-Based Test Execution
* Enhanced Self-Healing Capabilities

---

## Team Members

* Jayarani M
* Harshini T
* Hemadharshini M
* Hrithickram R

---

## About

TestForge AI demonstrates how Agentic AI and Multi-LLM collaboration can modernize software testing by automating test generation, execution, bug analysis, and QA decision-making.
