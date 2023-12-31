from flask import Flask
from home import home_bp
from contact import contact_bp
from test import test_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
app.register_blueprint(test_bp, url_prefix='/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)