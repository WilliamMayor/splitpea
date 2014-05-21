from flask import (
    Flask, render_template, redirect,
    url_for)

from assets import assets

app = Flask(__name__)
assets.init_app(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login/')
def login():
    return redirect(url_for('home'))

@app.route('/logout/')
def logout():
    return redirect(url_for('home'))

@app.route('/about/')
def about():
    return redirect(url_for('home'))

@app.route('/directory/')
def directory():
    return redirect(url_for('home'))

@app.route('/account/')
def account():
    return redirect(url_for('home'))

if  __name__ == '__main__':
    app.run(debug=True)
