from flask import Flask
from flask import render_template
from myblog_index import main as myblog_routes
from user import main as user_routes
from api import main as api_routes


app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'r2a4n5d&o/m? /s(t)r*i&n^g@'
# ?
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
app.register_blueprint(myblog_routes)
app.register_blueprint(user_routes)
app.register_blueprint(api_routes, url_prefix='/api')


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)