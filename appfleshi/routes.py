from flask import render_template
from appfleshi import app


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    return render_template('profile.html', username=username)