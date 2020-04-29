from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('/index')
@app.route('/home')
def hello():
    return "welcome to my watchlist"

@app.route('/user/<name>')
def  user_page(name):
    return '{0}'s page'.formate(name)