import pytest

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="https://dummyjson.com")