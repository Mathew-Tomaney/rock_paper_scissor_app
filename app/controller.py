from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def index():
    return render_template("index.html", title= "Home")

@app.route('/rules')
def rules():
    return render_template("rules.html", title="Rules")

@app.route('/2_players')
def two_players():
    return render_template("2_players.html", title="2-Player Game")

@app.route('/1_player')
def one_player():
    return render_template("1_player.html", title="1-Player Game")


@app.route('/play', methods=['POST'])
def play():
    player_1 = request.form['player_1']
    choice_1 = request.form['choice_1']
    player_2 = request.form['player_2']
    choice_2 = request.form['choice_2']
    game = Game(Player(player_1, choice_1), Player(player_2, choice_2))
    winning_player = game.play()
    result = game.show_results()
    
    
    return render_template("results.html", title="Results", winning_player= winning_player, game_result= result)

