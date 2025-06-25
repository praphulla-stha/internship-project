import pytest
import allure

def pytest_runtest_makereport(item, call):
    # Allure metadata
    test_id = item.nodeid.split("::")[-1]
    descriptions = {
        'test_create_product': 'Create a new product',
        'test_get_product': 'Retrieve a product by ID',
        'test_update_product': 'Update an existing product',
        'test_delete_product': 'Delete a product',
        'test_create_user': 'Create a new user',
        'test_get_user': 'Retrieve a user by ID',
        'test_update_user': 'Update an existing user',
        'test_delete_user': 'Delete a user',
        'test_create_user_invalid_data': 'Test user creation with invalid data',
        'test_create_post': 'Create a new post',
        'test_get_post': 'Retrieve a post by ID',
        'test_update_post': 'Update an existing post',
        'test_delete_post': 'Delete a post',
        'test_create_cart': 'Create a new cart',
        'test_get_cart': 'Retrieve a cart by ID',
        'test_update_cart': 'Update an existing cart',
        'test_delete_cart': 'Delete a cart',
        'test_create_comment': 'Create a new comment',
        'test_get_comment': 'Retrieve a comment by ID',
        'test_update_comment': 'Update an existing comment',
        'test_delete_comment': 'Delete a comment',
        'test_create_todo': 'Create a new todo',
        'test_get_todo': 'Retrieve a todo by ID',
        'test_update_todo': 'Update an existing todo',
        'test_delete_todo': 'Delete a todo'
    }
    allure.dynamic.title(test_id)
    allure.dynamic.description(descriptions.get(test_id, "No description"))
    allure.dynamic.feature("DummyJSON API")
    allure.dynamic.story(test_id.replace("test_", "").replace("_", " ").title())