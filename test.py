from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
test_bp = Blueprint('test', __name__)


@test_bp.before_request
def before():
    print ("This is executed before each request")
    
@test_bp.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

''' checking int passthrough'''
@test_bp.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number + 1)

''' checking string passthrough'''
@test_bp.route('/<string:name>/')
def hello(name):
    return "Hello " + name

''' checking json object'''
@test_bp.route('/person/')
def person():
    return jsonify({'name':'jimit',
                    'address':'Iceland'})

''' checking list of numbers'''
@test_bp.route('/numbers')
def print_list():
    return jsonify(list(range(5)))

''' looking into redirection behaviour /test/ vs /test '''
@test_bp.route('/home/')
def home():
    return "Home page"

@test_bp.route('/contact')
def contact():
    return "Contct page"

''' return status code'''
@test_bp.route('/status')
def status():
    return "would you like to see 418", 418
