from flask import Flask,render_template
from flask import url_for
from flask import request

app = Flask(__name__)

name = 'Grey Li'
movies = [
{'title': 'My Neighbor Totoro', 'year': '1988'},
{'title': 'Dead Poets Society', 'year': '1989'},
{'title': 'A Perfect World', 'year': '1993'},
{'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'},
{'title': 'King of Comedy', 'year': '1999'},
{'title': 'Devils on the Doorstep', 'year': '1999'},
{'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
{"title":"Alicia Mccormick","year":1998"},
{"title":"Jacob Carter","year":2019"},
{"title":"Brian Martinez","year":1993"},
{"title":"Connie Morrison","year":1982"},
{"title":"Steven Wilkerson","year":1980"},
{"title":"Terry Johnson","year":1992"},
{"title":"Paula Davis","year":1981"},
{"title":"Erin Collins","year":2002"},
{"title":"Ryan Avery","year":1991"},
{"title":"Crystal Flores","year":2006"},
]
@app.route('/')
def index():
    return render_template('index.html', name=name,movies=movies)
'''
@app.route('/')

@app.route('/index')
@app.route('/home')
def hello():
    #不只是通过template，可以替换文件，通过？=也可以实现参数自定义
    name=request.args.get('name')
    return "welcome to my watchlist,hello {0}".format(name)
@app.route('/wjh')
def wjh():
    return '', 302, {'Location': 'http://127.0.0.1:5000/home?name=wjh'}

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


@app.route('/goback/<int:year>')
def go_back(year):
    return 'welcome go back to %d' % (2020-year)
    '''