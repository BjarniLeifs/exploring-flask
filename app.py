from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

''' checking int passthrough'''
@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number + 1)

''' checking string passthrough'''
@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

''' checking json object'''
@app.route('/person/')
def person():
    return jsonify({'name':'jimit',
                    'address':'Iceland'})
''' checking list of numbers'''
@app.route('/numbers')
def print_list():
    return jsonify(list(range(5)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)