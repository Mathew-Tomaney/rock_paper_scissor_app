import random
from app.models.player import Player

class Game:

    def __init__(self, player_1, player_2 = None):
        self.random = random.choice(["Rock", "Paper", "Scissors"])
        self.player_1 = player_1
        self.player_2 = player_2 if player_2 is not None else Player("Computer", self.random)
        self.winning_player = None

    def play(self):
        result = ((self.player_1.choice - self.player_2.choice) + 5 ) % 3 
        
        if result == 0:
            self.winning_player = self.player_1
        elif result == 1:
            self.winning_player = self.player_2
        return self.winning_player

    def show_results(self):
        if self.winning_player == None:
            return "It's a draw!"
        else:
            return f"{self.winning_player.name} wins by playing {self.winning_player.input_choice}!"

    