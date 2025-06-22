from .base_service import BaseService

class DummyJsonService(BaseService):
    def __init__(self, base_url):
        super().__init__(base_url)

    # Product endpoints
    def get_product(self, product_id):
        return self.get(f"products/{product_id}")

    def create_product(self, data):
        return self.post("products/add", data)

    def update_product(self, product_id, data):
        return self.put(f"products/{product_id}", data)

    def delete_product(self, product_id):
        return self.delete(f"products/{product_id}")

    # User endpoints
    def get_user(self, user_id):
        return self.get(f"users/{user_id}")

    def create_user(self, data):
        return self.post("users/add", data)

    def update_user(self, user_id, data):
        return self.put(f"users/{user_id}", data)

    def delete_user(self, user_id):
        return self.delete(f"users/{user_id}")

    # Post endpoints
    def get_post(self, post_id):
        return self.get(f"posts/{post_id}")

    def create_post(self, data):
        return self.post("posts/add", data)

    def update_post(self, post_id, data):
        return self.put(f"posts/{post_id}", data)

    def delete_post(self, post_id):
        return self.delete(f"posts/{post_id}")

    # Cart endpoints
    def get_cart(self, cart_id):
        return self.get(f"carts/{cart_id}")

    def create_cart(self, data):
        return self.post("carts/add", data)

    def update_cart(self, cart_id, data):
        return self.put(f"carts/{cart_id}", data)

    def delete_cart(self, cart_id):
        return self.delete(f"carts/{cart_id}")

    # Comment endpoints
    def get_comment(self, comment_id):
        return self.get(f"comments/{comment_id}")

    def create_comment(self, data):
        return self.post("comments/add", data)

    def update_comment(self, comment_id, data):
        return self.put(f"comments/{comment_id}", data)

    def delete_comment(self, comment_id):
        return self.delete(f"comments/{comment_id}")

    # Todo endpoints
    def get_todo(self, todo_id):
        return self.get(f"todos/{todo_id}")

    def create_todo(self, data):
        return self.post("todos/add", data)

    def update_todo(self, todo_id, data):
        return self.put(f"todos/{todo_id}", data)

    def delete_todo(self, todo_id):
        return self.delete(f"todos/{todo_id}")