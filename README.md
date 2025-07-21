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


---


---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/praphulla-stha/internship-project.git
cd api-testing-framework
```
### 2. Install dependencies
```bash
pip install pipenv
pipenv install
```

### 3. Configure environment variables
```bash
Create a .env file and add:
BASE_URL=https://your.api.endpoint/
```
### 4. Run tests
```bash
pipenv run pytest --alluredir=allure-results
```

### 5. Generate Allure report
```bash
allure serve allure-results
```

