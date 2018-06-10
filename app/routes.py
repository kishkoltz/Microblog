from flask import render_template, flash, redirect
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
    return render_template('/index',
    title = 'Home', user = user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('/login', title='Sign In', form=form)
