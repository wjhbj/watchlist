from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')

@app.route('/index')
@app.route('/home')
def hello():
    name=request.args.get('name','Flask')
    return "welcome to my watchlist,hello {0}".format(name)

@app.route('/user/<name>')
def  user_page(name):
    return '{0}\'s page'.format(name)

@app.route('/test')
def test_url_for():
    #下面一些调用示例，（请在命令行查看结果）
    print(url_for('hello'))
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli')) # 输出：/user/greyli
    print(url_for('user_page', name='peter')) # 输出：/user/peter
    print(url_for('test_url_for')) # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2)) # 输出：/test?num=2
    return 'Test page'