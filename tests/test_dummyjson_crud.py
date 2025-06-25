import pytest
import logging
import allure
from services.dummyjson_service import DummyJsonService
from utils.file_reader import read_json_file
from config import BASE_URL

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def service():
    return DummyJsonService(BASE_URL)

# Product Tests
@allure.feature("DummyJSON API")
@allure.story("Create a new product")
def test_create_product(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read product data"):
        data = read_json_file("data/create_product.json")
        logger.info(f"Creating product with data: {data}")
    with allure.step("Send create product request"):
        response = service.create_product(data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id"), "Product creation failed"
        assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
        assert response["price"] == data["price"], f"Expected price {data['price']}, got {response['price']}"

@allure.feature("DummyJSON API")
@allure.story("Retrieve a product by ID")
def test_get_product(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send get product request"):
        logger.info("Retrieving product with ID 1")
        response = service.get_product(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Failed to retrieve product"
        assert "title" in response, "Product title not found"
        assert "price" in response, "Product price not found"

@allure.feature("DummyJSON API")
@allure.story("Update an existing product")
def test_update_product(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read update product data"):
        data = read_json_file("data/update_product.json")
        logger.info(f"Updating product with data: {data}")
    with allure.step("Send update product request"):
        response = service.update_product(1, data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Product update failed"
        assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
        assert response["price"] == data["price"], f"Expected price {data['price']}, got {response['price']}"

@allure.feature("DummyJSON API")
@allure.story("Delete a product")
def test_delete_product(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send delete product request"):
        logger.info("Deleting product with ID 1")
        response = service.delete_product(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Product deletion failed"
        assert response.get("isDeleted"), "Product not marked as deleted"

# User Tests
@allure.feature("DummyJSON API")
@allure.story("Create a new user")
def test_create_user(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read user data"):
        data = read_json_file("data/create_user.json")
        logger.info(f"Creating user with data: {data}")
    with allure.step("Send create user request"):
        response = service.create_user(data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id"), "User creation failed"
        assert response["firstName"] == data["firstName"], f"Expected firstName {data['firstName']}, got {response['firstName']}"
        assert response["email"] == data["email"], f"Expected email {data['email']}, got {response['email']}"

@allure.feature("DummyJSON API")
@allure.story("Retrieve a user by ID")
def test_get_user(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send get user request"):
        logger.info("Retrieving user with ID 1")
        response = service.get_user(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Failed to retrieve user"
        assert "firstName" in response, "User firstName not found"
        assert "email" in response, "User email not found"

@allure.feature("DummyJSON API")
@allure.story("Update an existing user")
def test_update_user(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read update user data"):
        data = read_json_file("data/update_user.json")
        logger.info(f"Updating user with data: {data}")
    with allure.step("Send update user request"):
        response = service.update_user(1, data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "User update failed"
        assert response["firstName"] == data["firstName"], f"Expected firstName {data['firstName']}, got {response['firstName']}"
        assert response["email"] == data["email"], f"Expected email {data['email']}, got {response['email']}"

@allure.feature("DummyJSON API")
@allure.story("Delete a user")
def test_delete_user(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send delete user request"):
        logger.info("Deleting user with ID 1")
        response = service.delete_user(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "User deletion failed"
        assert response.get("isDeleted"), "User not marked as deleted"

@allure.feature("DummyJSON API")
@allure.story("Test user creation with invalid data")
def test_create_user_invalid_data(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Prepare invalid user data"):
        invalid_data = {"firstName": "", "email": "invalid"}
        logger.info(f"Creating user with invalid data: {invalid_data}")
    with allure.step("Send create user request with invalid data"):
        try:
            response = service.create_user(invalid_data)
            logger.info(f"Response: {response}")
            allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
            assert False, "Expected user creation to fail with invalid data"
        except Exception as e:
            logger.info(f"Expected error: {str(e)}")
            allure.attach(str(e), name="Error Message", attachment_type=allure.attachment_type.TEXT)
            assert "error" in str(e).lower(), "Expected an error for invalid data"

# Post Tests
@allure.feature("DummyJSON API")
@allure.story("Create a new post")
def test_create_post(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read post data"):
        data = read_json_file("data/create_post.json")
        logger.info(f"Creating post with data: {data}")
    with allure.step("Send create post request"):
        response = service.create_post(data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id"), "Post creation failed"
        assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
        assert response["userId"] == data["userId"], f"Expected userId {data['userId']}, got {response['userId']}"

@allure.feature("DummyJSON API")
@allure.story("Retrieve a post by ID")
def test_get_post(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send get post request"):
        logger.info("Retrieving post with ID 1")
        response = service.get_post(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Failed to retrieve post"
        assert "title" in response, "Post title not found"
        assert "body" in response, "Post body not found"

@allure.feature("DummyJSON API")
@allure.story("Update an existing post")
def test_update_post(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read update post data"):
        data = read_json_file("data/update_post.json")
        logger.info(f"Updating post with data: {data}")
    with allure.step("Send update post request"):
        response = service.update_post(1, data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Post update failed"
        assert response["title"] == data["title"], f"Expected title {data['title']}, got {response['title']}"
        assert response["body"] == data["body"], f"Expected body {data['body']}, got {response['body']}"

@allure.feature("DummyJSON API")
@allure.story("Delete a post")
def test_delete_post(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send delete post request"):
        logger.info("Deleting post with ID 1")
        response = service.delete_post(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Post deletion failed"
        assert response.get("isDeleted"), "Post not marked as deleted"

# Cart Tests
@allure.feature("DummyJSON API")
@allure.story("Create a new cart")
def test_create_cart(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read cart data"):
        data = read_json_file("data/create_cart.json")
        logger.info(f"Creating cart with data: {data}")
    with allure.step("Send create cart request"):
        response = service.create_cart(data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id"), "Cart creation failed"
        assert response["userId"] == data["userId"], f"Expected userId {data['userId']}, got {response['userId']}"
        assert len(response["products"]) == len(data["products"]), "Product count mismatch"

@allure.feature("DummyJSON API")
@allure.story("Retrieve a cart by ID")
def test_get_cart(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send get cart request"):
        logger.info("Retrieving cart with ID 1")
        response = service.get_cart(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Failed to retrieve cart"
        assert "products" in response, "Cart products not found"
        assert "userId" in response, "Cart userId not found"

@allure.feature("DummyJSON API")
@allure.story("Update an existing cart")
def test_update_cart(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read update cart data"):
        data = read_json_file("data/update_cart.json")
        logger.info(f"Updating cart with data: {data}")
    with allure.step("Send update cart request"):
        response = service.update_cart(1, data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Cart update failed"
        assert len(response["products"]) == len(data["products"]), "Product count mismatch"
        assert response["products"][0]["id"] == data["products"][0]["id"], "Product ID mismatch"

@allure.feature("DummyJSON API")
@allure.story("Delete a cart")
def test_delete_cart(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send delete cart request"):
        logger.info("Deleting cart with ID 1")
        response = service.delete_cart(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Cart deletion failed"
        assert response.get("isDeleted"), "Cart not marked as deleted"

# Comment Tests
@allure.feature("DummyJSON API")
@allure.story("Create a new comment")
def test_create_comment(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read comment data"):
        data = read_json_file("data/create_comment.json")
        logger.info(f"Creating comment with data: {data}")
    with allure.step("Send create comment request"):
        response = service.create_comment(data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id"), "Comment creation failed"
        assert response["body"] == data["body"], f"Expected body {data['body']}, got {response['body']}"
        assert response["postId"] == data["postId"], f"Expected postId {data['postId']}, got {response['postId']}"

@allure.feature("DummyJSON API")
@allure.story("Retrieve a comment by ID")
def test_get_comment(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send get comment request"):
        logger.info("Retrieving comment with ID 1")
        response = service.get_comment(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Failed to retrieve comment"
        assert "body" in response, "Comment body not found"
        assert "postId" in response, "Comment postId not found"

@allure.feature("DummyJSON API")
@allure.story("Update an existing comment")
def test_update_comment(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read update comment data"):
        data = read_json_file("data/update_comment.json")
        logger.info(f"Updating comment with data: {data}")
    with allure.step("Send update comment request"):
        response = service.update_comment(1, data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Comment update failed"
        assert response["body"] == data["body"], f"Expected body {data['body']}, got {response['body']}"

@allure.feature("DummyJSON API")
@allure.story("Delete a comment")
def test_delete_comment(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send delete comment request"):
        logger.info("Deleting comment with ID 1")
        response = service.delete_comment(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Comment deletion failed"
        assert response.get("isDeleted"), "Comment not marked as deleted"

# Todo Tests
@allure.feature("DummyJSON API")
@allure.story("Create a new todo")
def test_create_todo(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read todo data"):
        data = read_json_file("data/create_todo.json")
        logger.info(f"Creating todo with data: {data}")
    with allure.step("Send create todo request"):
        response = service.create_todo(data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id"), "Todo creation failed"
        assert response["todo"] == data["todo"], f"Expected todo {data['todo']}, got {response['todo']}"
        assert response["completed"] == data["completed"], f"Expected completed {data['completed']}, got {response['completed']}"

@allure.feature("DummyJSON API")
@allure.story("Retrieve a todo by ID")
def test_get_todo(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send get todo request"):
        logger.info("Retrieving todo with ID 1")
        response = service.get_todo(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Failed to retrieve todo"
        assert "todo" in response, "Todo task not found"
        assert "completed" in response, "Todo completed status not found"

@allure.feature("DummyJSON API")
@allure.story("Update an existing todo")
def test_update_todo(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Read update todo data"):
        data = read_json_file("data/update_todo.json")
        logger.info(f"Updating todo with data: {data}")
    with allure.step("Send update todo request"):
        response = service.update_todo(1, data)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Todo update failed"
        assert response["todo"] == data["todo"], f"Expected todo {data['todo']}, got {response['todo']}"
        assert response["completed"] == data["completed"], f"Expected completed {data['completed']}, got {response['completed']}"

@allure.feature("DummyJSON API")
@allure.story("Delete a todo")
def test_delete_todo(service, caplog):
    caplog.set_level(logging.INFO)
    with allure.step("Send delete todo request"):
        logger.info("Deleting todo with ID 1")
        response = service.delete_todo(1)
        logger.info(f"Response: {response}")
        allure.attach(str(response), name="Response JSON", attachment_type=allure.attachment_type.JSON)
    with allure.step("Validate response"):
        assert response.get("id") == 1, "Todo deletion failed"
        assert response.get("isDeleted"), "Todo not marked as deleted"