from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.before_request
def before():
    print ("This is executed before each request")
    
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

''' looking into redirection behaviour /test/ vs /test '''
@app.route('/home/')
def home():
    return "Home page"

@app.route('/contact')
def contact():
    return "Contct page"

''' return status code'''
@app.route('/status')
def status():
    return "would you like to see 418", 418

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)