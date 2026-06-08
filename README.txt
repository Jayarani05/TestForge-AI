#  TestForge AI

Agentic AI Powered QA Automation Platform - Convert requirements into optimized test cases, execute automation scripts, analyze bugs, repair failed tests, generate CI/CD pipelines, analyze repositories, and export QA reports using intelligent AI agents.

Built with **React, FastAPI, Python, SQLite, Gemini, Llama, DeepSeek, and Agentic AI workflows**.


![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![AI](https://img.shields.io/badge/Agentic-AI-purple)
![LLM](https://img.shields.io/badge/MultiLLM-Gemini%20%7C%20Llama%20%7C%20DeepSeek-orange)


---

# 📸 Project Screenshots

(Add screenshots here)

```
Output/screenshots/
```

---

#  System Architecture

TestForge AI follows an Agentic AI architecture where specialized AI agents collaborate to automate the complete QA engineering lifecycle.


```
                 User Requirement

                        |
                        v

              Requirement Agent

                        |
                        v

            Multi LLM Orchestrator


        Gemini       Llama       DeepSeek

            \          |          /

                    Judge Agent

                        |
                        v

             Optimized QA Response


                        |
 ------------------------------------------------
 |              |              |                 |
Test        Execution       Bug             DevOps
Agent        Agent        Analyzer          Agent


                        |
                        v

                 QA Automation Output
```


---

#  Features


| Feature | Description |
|---|---|
|  Authentication | JWT secured user authentication |
|  Dashboard | QA analytics overview |
|  Project Management | Maintain QA projects separately |
|  Requirement Agent | Understands user stories and requirements |
|  Multi LLM Engine | Uses Gemini, Llama, and DeepSeek |
|  Judge Agent | Selects highest quality AI response |
|  Test Generator | Creates automation test scenarios |
|  Test Execution | Executes generated test scripts |
|  Bug Analyzer | Detects root cause of failures |
|  Self Healing | Repairs broken Selenium locators |
|  Repository Intelligence | Analyzes GitHub repositories |
|  CI/CD Generator | Creates DevOps pipelines |
|  Export Center | Generates QA reports |


---

#  AI Agents


## Requirement Agent

Analyzes:

- User stories
- Requirements
- Risks
- Testing scope


---

## Test Generation Agent

Generates:

- Positive tests
- Negative tests
- Edge cases
- Security scenarios


---

## Multi LLM Orchestrator


Connected Models:

- Google Gemini
- Llama
- DeepSeek


Each model produces independent outputs.


---

## Judge Agent


Evaluates using:

- Accuracy
- Coverage
- Code quality
- Completeness


Selects the best result.


---

## Test Execution Agent

Handles:

- Running automation scripts
- Capturing logs
- Execution status


---

## Bug Analyzer Agent

Finds:

- Severity
- Root cause
- Fix suggestion
- QA recommendation


---

## Self Healing Agent

Automatically fixes:

- Broken locators
- DOM changes
- Failed Selenium scripts


---

## Repository Agent

Analyzes:

- Technology stack
- Code structure
- Security issues
- Improvements


---

## CI/CD Agent

Generates:

- GitHub Actions workflows
- Test pipelines
- Automation setup


---

#  How It Works


Example:


User Input:


```
As a customer,
I want to add products to cart,
update quantity,
remove products,
and complete checkout.
```


Flow:


```
Requirement

 ↓

Requirement Agent

 ↓

Gemini | Llama | DeepSeek

 ↓

Judge Agent

 ↓

Generated QA Test Cases

 ↓

Execution + Analysis + Reports
```


---

#  Tech Stack


## Frontend

- React JS
- Tailwind CSS
- Axios
- Lucide React


## Backend

- Python
- FastAPI
- SQLAlchemy
- JWT Authentication


## Database

- SQLite


## AI / LLM

- Gemini API
- Llama
- DeepSeek
- Agentic AI Design


## Testing

- Pytest
- Selenium


---

#  Project Structure


```
TestForge-AI

│
├── Backend
│
│   └── app
│        |
│        ├── agents
│        ├── api
│        ├── database
│        ├── security
│        └── llm_services
│
│
├── Frontend
│
│   └── src
│        |
│        ├── pages
│        ├── components
│        └── api
│
│
├── Documents
│
│   ├── AI_USAGE.md
│   ├── DEMO.md
│   └── Test_Cases.md
│
│
├── sample_data
│
├── Output
│
├── README.md
│
└── .gitignore
```


---

#  Quick Start


## Backend Setup


```bash
cd Backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```


Backend:


```
http://127.0.0.1:8000
```


---

## Frontend Setup


```bash
cd Frontend

npm install

npm run dev
```


Frontend:


```
http://localhost:5173
```


---

#  Sample Inputs


## Test Generator


```
Generate automation tests for ecommerce checkout workflow.
```


---

## Bug Analyzer


```
AssertionError:

Expected status code 200 but received 500.

JWT authentication failed.
```


---

## Self Healing


Broken Code:


```python
driver.find_element(
"id",
"old-login-button"
).click()
```


Updated DOM:


```html
<button id="new-login-button">
Login
</button>
```


---

#  Documentation


Available in:

```
Documents/
```


Contains:

- AI_USAGE.md
- DEMO.md
- Test_Cases.md


---

#  Security


- JWT Authentication
- Protected APIs
- Environment variables
- User based authorization
- Secure AI access


---

#  Run Tests


```bash
pytest
```


---

#  Demo Video


Watch Demo Video:

https://drive.google.com/drive/folders/1MMhRRGd6zoAp46JXAaSimzBJfuoONZvg


---

#  Contributors


| Name | Contribution |
|---|---|
| Jayarani M | Agentic AI Architecture & Full Stack Development |
| Harshini T | AI Agent Development & Testing |
| Hemadharshini M | Backend Development & Integration |
| Hrithickram R | Frontend Development & UI Integration |



---

#  Future Enhancements


- Cloud deployment
- Real browser automation execution
- Advanced QA analytics
- More LLM integrations
- Enterprise test management


---

#  About

TestForge AI demonstrates how Agentic AI and Multi LLM collaboration can transform traditional QA automation by reducing manual testing effort and improving software quality.
