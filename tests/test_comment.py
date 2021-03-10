import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Collins = User(first_name = "George",
                                last_name = "Kilewa",
                                username = "Georgek",
                                password = "moringa",
                                email = "kilewageorge230@gmail.com")
        self.new_post = Post(post_title = "Test Title",
                            post_content = "This is a great move. I love blogging!",
                            user_id = self.user_George.id)
        self.new_comment = Comment(comment = "Great one!",
                                    post_id = self.new_post.id,
                                    user_id = self.user_George.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_George, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))
