'''
This right now contains the global app instance which is referenced by
controllers / server.py
'''

from flask import Flask
app = Flask(__name__)
app.secret_key = "top_secret_dont_tell"
