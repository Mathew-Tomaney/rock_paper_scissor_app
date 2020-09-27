from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def rules():
    return render_template("index.html", title= "Rules")


@app.route('/play', methods=['POST'])
def play():
    player_1 = request.form['player_1']
    choice_1 = request.form['choice_1']
    player_2 = request.form['player_2']
    choice_2 = request.form['choice_2']
    result = Game(Player(player_1, choice_1), Player(player_2, choice_2)).play()
    
    return render_template("index.html", title="Rock Paper Scissors", game_result= result)

