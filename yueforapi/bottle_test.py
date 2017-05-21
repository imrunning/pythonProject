from bottle import route, run, template, request
from datetime import datetime
import json
@route('/')
def index(name='time'):
     dt = datetime.now()
     time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
     return template('<b>Pi think the date/time is:{{t}}</b>', t = time)
@route('/apitest/<input>')
def hello(input):
    data = [{'a': "A", 'b': (2, 4), 'c': 3.0}]
    json_string = json.dumps(data)
    return 'hello world '+ input + json_string
@route('/apitest')
def loginapi():
    userName = request.GET.get('userName')
    password = request.GET.get('password')
    return 'userName:' + userName+ 'password ' + password
run(host='localhost',port = 8090)