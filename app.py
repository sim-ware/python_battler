from flask import Flask, request
from flask import render_template
# import test
import json
import requests
import random
app = Flask(__name__)


##
# Index/Home Route
##################
@app.route('/battler', methods=['GET'])
@app.route('/')
def index():
    return render_template('home.html')
