from flask import flask

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    retirm "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)