from bottle import route, run, template
from datetime import datetime
import json
@route('/')
def index(name='time'):
     dt = datetime.now()
     time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
     return template('<b>Pi think the date/time is:{{t}}</b>', t = time)
@route('/apitest/:input')
def hello(input):
    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
    parse_json = json.load(json_string)
    return 'hello world '+ input + parse_json["first_name"]
run(host='192.168.0.116',port = 8090)