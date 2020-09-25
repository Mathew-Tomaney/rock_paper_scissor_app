from flask import render_template
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/<player_1>/<choice_1>/<player_2>/<choice_2>')
def index(player_1, choice_1, player_2, choice_2):
    result = Game(Player(player_1, choice_1), Player(player_2, choice_2)).play()
    
    return render_template("index.html", title="Rock Paper Scissors", game_result= result)

