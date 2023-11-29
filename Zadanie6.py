from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>Hello, choose a method inside your URL uśmiech</h1>'

@app.route("/titles", methods=["GET"])
def titles():
    with open('animations.json') as json_data:
        result = []
        data = json.load(json_data)
        for animation in data['animations']:
            result.append(animation['Original title'])
    if 'from' in request.args and 'to' in request.args:
        result_new = []
        xyz = int(request.args['from'])
        abc = int(request.args['to'])
        for animation in data['animations']:
            if xyz <= animation['Year of production'] <= abc:
                result_new.append(animation['Original title'])
        return result_new
    return result

@app.route("/directors/<expression>", methods=["GET"])
def directors(expression):
    with open('animations.json') as json_data:
        result = []
        data = json.load(json_data)
        for animation in data['animations']:
            if expression.lower() in animation['Directors'].lower():
                result.append(animation['Directors'])
    return result