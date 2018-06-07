from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Chris'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Wow, Chris is learning Flask!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I wonder if the Han Solo movie is any good.'
        }
    ]
    return render_template('index.html',
    title = 'Home', user = user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
