from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "这是首页"

@app.route("/login/")
def login():
    return "登录成功"

@app.route("/projects/")
def projects():
    return "这是projects"

app.run(debug=True)