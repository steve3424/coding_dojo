'''
Contains the global app object.

It only gets run once no matter how many times it is imported.

'''

from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "secrets"
bcrypt = Bcrypt(app)