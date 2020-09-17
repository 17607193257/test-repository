
#0.导包
from httprunner.api import HttpRunner

#1.创建Httprunner对象
runner = HttpRunner()

#2.运行用例
runner.run(r"E:\TEST\07python19\HttpRunnerLemon\testsuites\demo_testsuite.yml")

print(runner.summary)


