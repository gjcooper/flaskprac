from flask import render_template
from app import app


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
