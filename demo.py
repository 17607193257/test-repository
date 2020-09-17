from wsgiref.simple_server import make_server


def app(env,response):  #env：环境变量，浏览器传递进来的参数web服务器会保存在本地的环境变量中，处理程序聪本地获取环境变量
    print("正在监听")
    response("200 ok",[("content-type","text/html")])
    return [b"this is a demo"]  #b：返回的是二进制的列表


#初始化一个服务器
server = make_server("",5200,app) #服务器地址、端口、处理程序
server.serve_forever(0.2) #poll_interval轮询时间，间隔多长时间去刷新请求
