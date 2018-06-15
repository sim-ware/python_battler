from flask import Flask, request
from flask import render_template
from flask import jsonify
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


##
# Results Route
###############
@app.route('/gamestate', methods=['POST'])
def resultloop():
    player_one = request.form['player_one_name']
    # player_two = request.form['player_two_name'] if request.form['player_two_name'] else player_two = 'Computer'
    if request.form['player_two_name']:
        player_two = request.form['player_two_name']
    else:
        player_two = 'Computer'
    # 'Yes' if fruit == 'Apple' else 'No'
    return render_template('gamestate.html', pOne=player_one, pTwo=player_two)
# @app.route('/background_process')
# def background_process():
# 	try:
# 		lang = request.args.get('proglang', 0, type=str)
# 		if lang.lower() == 'python':
# 			return jsonify(result='You are wise')
# 		else:
# 			return jsonify(result='Try again.')
# 	except Exception as e:
# 		return str(e)

# @app.route('/resultloop', methods=['POST'])
# def resultloop():
#     searchterms = request.form['searchterms']
#     r = requests.get(("http://api.giphy.com/v1/gifs/search?q="
#                     + searchterms
#                     + "&api_key=02KjSiPr9Ur2Hizm8HsEdgB0NXPJiNBh&limit=50"))
#     r = r.json()
#     gifs_list = []
#     for x in range(50):
#         a = r['data'][x]['images']['original']['url']
#         gifs_list.append(a)
#     randomers = random.sample(range(50), 25)
#     resultloop = [gifs_list[i] for i in randomers]
#     return render_template('resultloop.html', resultloop=resultloop)
