# 🔍 Automated API Testing Framework with Continuous Integration

This project is a Python-based API testing framework designed to automate the testing of RESTful APIs. It includes modular test cases, rich reporting with Allure, and integration with GitHub Actions for continuous testing.

---

## 📌 Features

- ✅ Test automation for CRUD operations across multiple endpoints
- ⚙️ Built using Pytest and Requests
- 📊 Interactive HTML reports using Allure
- 🔁 CI pipeline with GitHub Actions
- 🔐 Environment configuration via `.env` file

---

## 🧰 Tools & Technologies Used

| Category        | Tools/Technologies |
|----------------|--------------------|
| Language        | Python             |
| Testing         | Pytest, Postman    |
| API Handling    | Requests Library   |
| Reporting       | Allure Framework   |
| CI/CD           | GitHub Actions     |
| Environment Mgmt| python-dotenv, Pipenv |
| Test Mgmt       | TestRail (externally) |
| Bug Tracking    | JIRA (externally)   |

---

## 📂 Project Structure
.
├── tests/ # Test cases
├── services/ # API request handling
├── utils/ # Utility functions
├── data/ # Test payloads (JSON)
├── config/ # Environment and setup files
├── .env # API base URL and secrets
├── Pipfile # Dependencies
└── .github/workflows/ # CI pipeline (GitHub Actions)


---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/praphulla-stha/internship-project.git
cd api-testing-framework

### 2. Install dependencies
pip install pipenv
pipenv install

### 3. Configure environment variables
Create a .env file and add:
BASE_URL=https://your.api.endpoint/

### 4. Run tests
pipenv run pytest --alluredir=allure-results

### 5. Generate Allure report
allure serve allure-results

🧠 Learning Outcomes
Hands-on experience with automated testing using Python

CI/CD setup using GitHub Actions

End-to-end API validation with logging and reporting

Working with professional tools like Postman, JIRA, and TestRail