from bottle import route, run, template
from datetime import datetime
@route('/')
def index(name='time'):
     dt = datetime.now()
     time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
     return template('<b>Pi think the date/time is:{{t}}</b>', t = time)
@route('/apitest/:input')
def hello(input):
        return 'hello world '+ input
run(host='192.168.0.116',port = 8090)