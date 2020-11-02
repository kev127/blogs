from app.models import User,Blog
from app import db
from app import app
import unittest

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_kev = User(username = 'kev',password = '@Y0a!yAV', email = 'kelvinkeya125@gmail.com')
        self.new_blog = Blog(id=1,blog_title='blog',blog_content='welcome to my blog',category="life",user = self.user_kelvin,likes=0,dislikes=0)

    def tearDown(self):
        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()
      

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_title,'blog')
        self.assertEquals(self.new_blog.blog_content,'welcome to my blog')
        self.assertEquals(self.new_blog.category,"life")
        self.assertEquals(self.new_blog.
        user,self.user_Peris)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blog= Blig.get_blog(1)
        self.assertTrue(got_blog is not None)