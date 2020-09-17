from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/login/")
def inde():
    print("login success")
    return "login success！!"

# @app.route("/projects/",methods=["get","post"])
# def project():
#     return "projects!"

@app.route("/projects/<id>")
def project(id):
    return f"projects{id}!"

@app.route("/projects/")
def project():
    id = request.args.get("id")
    return f"projects{id}!"
    # return str(id)
#启动web服务，可以用gunicorn,uwsgi,也可以用flask自带的web服务run
#生产环境不要用flask自带的web服务
#debug模式有两个好处：1.程序有修改时，自动重启，2.显示错误信息
app.run(debug=True)