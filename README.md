DummyJSON API Automation Framework
A modular, scalable API testing framework for the DummyJSON API, built with Python, requests, and pytest. This framework automates CRUD (Create, Read, Update, Delete) operations for multiple endpoints (/products, /users, /posts, /carts), designed for QA engineers and developers.
Features

Modular Design: Separates services, tests, and utilities for easy maintenance.
Comprehensive Tests: Covers CRUD operations for multiple DummyJSON endpoints.
Scalable: Easily extendable to support additional APIs or endpoints.
Reporting: Generates HTML test reports using pytest-html.
Environment Configuration: Uses .env for flexible setup.

Prerequisites

Python 3.9 or higher
pipenv for dependency management
PowerShell or another terminal
IDE (e.g., VS Code, PyCharm)

Setup

Clone the Repository:
git clone <your-repo-url>
cd dummyjson-api-framework


Install Dependencies:
pip install pipenv
pipenv install


Set Up Environment:Create a .env file in the project root with:
BASE_URL=https://dummyjson.com


Activate Virtual Environment:
pipenv shell



Running Tests

Run All Tests:
cd tests
pipenv run pytest -v --html=report.html


Generates a report.html file with test results in the tests/ directory.


Run a Specific Test:Example for testing product creation:
pipenv run pytest test_dummyjson_crud.py::test_create_product -v


View Test Report:Open tests/report.html in a web browser to view detailed test results.


Project Structure
dummyjson-api-framework/
├── services/
│   ├── base_service.py        # Generic HTTP methods
│   ├── dummyjson_service.py   # DummyJSON API-specific methods
│   ├── __init__.py
├── tests/
│   ├── data/                 # JSON payloads for tests
│   │   ├── create_product.json
│   │   ├── update_product.json
│   │   ├── create_user.json
│   │   ├── update_user.json
│   │   ├── create_post.json
│   │   ├── update_post.json
│   │   ├── create_cart.json
│   │   ├── update_cart.json
│   ├── test_dummyjson_crud.py  # Test suite for CRUD operations
│   ├── __init__.py
├── utils/
│   ├── file_reader.py         # Reads JSON files
│   ├── request.py            # Handles HTTP requests
│   ├── __init__.py
├── .env                      # Environment variables
├── .gitignore                # Git ignore rules
├── config.py                 # Loads environment variables
├── conftest.py               # Pytest configuration
├── Pipfile                   # Dependency management
├── README.md                 # Project documentation

Extending the Framework
To add tests for new DummyJSON endpoints (e.g., /comments, /todos):

Add Service Methods:
In services/dummyjson_service.py, add methods like:def get_comment(self, comment_id):
    return self.get(f"comments/{comment_id}")




Create Test Data:
Add JSON files (e.g., tests/data/create_comment.json) with payloads.


Write Tests:
Add test cases in tests/test_dummyjson_crud.py, e.g.:def test_get_comment(service):
    response = service.get_comment(1)
    assert response.get("id") == 1, "Failed to retrieve comment"




Run Tests:Use the commands above to verify new tests.

Troubleshooting

Test Failures: Check logs in the terminal (from utils/request.py) for HTTP errors.
Dependency Issues: Ensure Pipfile dependencies are installed (pipenv install).
API Changes: Verify endpoint behavior at DummyJSON Docs.

License
MIT License (or specify your preferred license)
