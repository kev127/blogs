from flask import render_template,request,redirect,url_for
from . import main
from .forms import UpdateProfile, BlogForm, CommentForm
from ..models import User,Blog,Comment
from ..requests import get_quotes

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quotes= get_quotes()
    title = 'Home -welcome to Blogs'
    
    return render_template('index.html',title = title,quotes=quotes)