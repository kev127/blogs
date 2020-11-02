from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_Quotes
from ..models import User, Blog,Comment

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    Quote = get_Quotes()
    title = 'Home -welcome to My Blogs'
    
    return render_template('index.html',title = title, blogQuote=blogQuote)