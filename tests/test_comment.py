from app.models import Comment,User,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_kev = User(username = 'kev',password = '@Y0a!yAv', email = 'kelvinkeya125@gmail.com')
        self.new_blog = Blog(id=1,title_blog='blog',blog_content='welcome to my blog',category="life",user = self.user_kelvin)
        self.new_comment = Comment(id=1,comment='New comment',user=self.user_kelvin,blog=self.new_blog)

    def tearDown(self):
        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'New comment')
        self.assertEquals(self.new_comment.user,self.user_kelvin)
        self.assertEquals(self.new_comment.blog,self.new_blog)