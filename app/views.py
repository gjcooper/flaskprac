from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Gavin'}
    posts = [
        {
            'author': {'nickname': 'Coop'},
            'body': 'I totally love this guy man!'
        },
        {
            'author': {'nickname': 'Lish'},
            'body': 'I totally love my main man!'
        }
    ]

    return render_template('index.html', title='Base', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{}", remember_me={}'.format(
            form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, 
                           providers=app.config['OPENID_PROVIDERS'])
