import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Collins = User(first_name = "David",
                                last_name = "Hashisoma",
                                username = "@Hashi",
                                password = "hashi123",
                                email = "davidhashisoma95@gmail.com")
        self.new_post = Post(post_title = "Test Title",
                            post_content = "This is a great move. I love blogging!",
                            user_id = self.user_Hashisoma.id)
        self.new_comment = Comment(comment = "Great one!",
                                    post_id = self.new_post.id,
                                    user_id = self.user_George.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Hashisoma, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))
