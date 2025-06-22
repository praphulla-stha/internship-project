import pytest
from services.dummyjson_service import DummyJsonService
from utils.file_reader import read_json_file
from config import BASE_URL

@pytest.fixture
def service():
    return DummyJsonService(BASE_URL)

# Product Tests
def test_create_product(service):
    data = read_json_file("data/create_product.json")
    response = service.create_product(data)
    assert response.get("id"), "Product creation failed"
    assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
    assert response["price"] == data["price"], f"Expected price {data['price']}, got {response['price']}"

def test_get_product(service):
    response = service.get_product(1)
    assert response.get("id") == 1, "Failed to retrieve product"
    assert "title" in response, "Product title not found"
    assert "price" in response, "Product price not found"

def test_update_product(service):
    data = read_json_file("data/update_product.json")
    response = service.update_product(1, data)
    assert response.get("id") == 1, "Product update failed"
    assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
    assert response["price"] == data["price"], f"Expected price {data['price']}, got {response['price']}"

def test_delete_product(service):
    response = service.delete_product(1)
    assert response.get("id") == 1, "Product deletion failed"
    assert response.get("isDeleted"), "Product not marked as deleted"

# User Tests
def test_create_user(service):
    data = read_json_file("data/create_user.json")
    response = service.create_user(data)
    assert response.get("id"), "User creation failed"
    assert response["firstName"] == data["firstName"], f"Expected firstName {data['firstName']}, got {response['firstName']}"
    assert response["email"] == data["email"], f"Expected email {data['email']}, got {response['email']}"

def test_get_user(service):
    response = service.get_user(1)
    assert response.get("id") == 1, "Failed to retrieve user"
    assert "firstName" in response, "User firstName not found"
    assert "email" in response, "User email not found"

def test_update_user(service):
    data = read_json_file("data/update_user.json")
    response = service.update_user(1, data)
    assert response.get("id") == 1, "User update failed"
    assert response["firstName"] == data["firstName"], f"Expected firstName {data['firstName']}, got {response['firstName']}"
    assert response["email"] == data["email"], f"Expected email {data['email']}, got {response['email']}"

def test_delete_user(service):
    response = service.delete_user(1)
    assert response.get("id") == 1, "User deletion failed"
    assert response.get("isDeleted"), "User not marked as deleted"

# Post Tests
def test_create_post(service):
    data = read_json_file("data/create_post.json")
    response = service.create_post(data)
    assert response.get("id"), "Post creation failed"
    assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
    assert response["userId"] == data["userId"], f"Expected userId {data['userId']}, got {response['userId']}"

def test_get_post(service):
    response = service.get_post(1)
    assert response.get("id") == 1, "Failed to retrieve post"
    assert "title" in response, "Post title not found"
    assert "body" in response, "Post body not found"

def test_update_post(service):
    data = read_json_file("data/update_post.json")
    response = service.update_post(1, data)
    assert response.get("id") == 1, "Post update failed"
    assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
    assert response["body"] == data["body"], f"Expected body {data['body']}, got {response['body']}"

def test_delete_post(service):
    response = service.delete_post(1)
    assert response.get("id") == 1, "Post deletion failed"
    assert response.get("isDeleted"), "Post not marked as deleted"

# Cart Tests
def test_create_cart(service):
    data = read_json_file("data/create_cart.json")
    response = service.create_cart(data)
    assert response.get("id"), "Cart creation failed"
    assert response["userId"] == data["userId"], f"Expected userId {data['userId']}, got {response['userId']}"
    assert len(response["products"]) == len(data["products"]), "Product count mismatch"

def test_get_cart(service):
    response = service.get_cart(1)
    assert response.get("id") == 1, "Failed to retrieve cart"
    assert "products" in response, "Cart products not found"
    assert "userId" in response, "Cart userId not found"

def test_update_cart(service):
    data = read_json_file("data/update_cart.json")
    response = service.update_cart(1, data)
    assert response.get("id") == 1, "Cart update failed"
    assert len(response["products"]) == len(data["products"]), "Product count mismatch"
    assert response["products"][0]["id"] == data["products"][0]["id"], "Product ID mismatch"

def test_delete_cart(service):
    response = service.delete_cart(1)
    assert response.get("id") == 1, "Cart deletion failed"
    assert response.get("isDeleted"), "Cart not marked as deleted"

# Comment Tests
def test_create_comment(service):
    data = read_json_file("data/create_comment.json")
    response = service.create_comment(data)
    assert response.get("id"), "Comment creation failed"
    assert response["body"] == data["body"], f"Expected body {data['body']}, got {response['body']}"
    assert response["postId"] == data["postId"], f"Expected postId {data['postId']}, got {response['postId']}"

def test_get_comment(service):
    response = service.get_comment(1)
    assert response.get("id") == 1, "Failed to retrieve comment"
    assert "body" in response, "Comment body not found"
    assert "postId" in response, "Comment postId not found"

def test_update_comment(service):
    data = read_json_file("data/update_comment.json")
    response = service.update_comment(1, data)
    assert response.get("id") == 1, "Comment update failed"
    assert response["body"] == data["body"], f"Expected body {data['body']}, got {response['body']}"

def test_delete_comment(service):
    response = service.delete_comment(1)
    assert response.get("id") == 1, "Comment deletion failed"
    assert response.get("isDeleted"), "Comment not marked as deleted"

# Todo Tests
def test_create_todo(service):
    data = read_json_file("data/create_todo.json")
    response = service.create_todo(data)
    assert response.get("id"), "Todo creation failed"
    assert response["todo"] == data["todo"], f"Expected todo {data['todo']}, got {response['todo']}"
    assert response["completed"] == data["completed"], f"Expected completed {data['completed']}, got {response['completed']}"

def test_get_todo(service):
    response = service.get_todo(1)
    assert response.get("id") == 1, "Failed to retrieve todo"
    assert "todo" in response, "Todo task not found"
    assert "completed" in response, "Todo completed status not found"

def test_update_todo(service):
    data = read_json_file("data/update_todo.json")
    response = service.update_todo(1, data)
    assert response.get("id") == 1, "Todo update failed"
    assert response["todo"] == data["todo"], f"Expected todo {data['todo']}, got {response['todo']}"
    assert response["completed"] == data["completed"], f"Expected completed {data['completed']}, got {response['completed']}"

def test_delete_todo(service):
    response = service.delete_todo(1)
    assert response.get("id") == 1, "Todo deletion failed"
    assert response.get("isDeleted"), "Todo not marked as deleted"