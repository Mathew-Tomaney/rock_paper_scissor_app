import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(self):
    
    def setUp(self):
        self.game_1 = Game(Player("Hal", "Rock"), Player("Dave", "Scissors"))

    def test_game_has_player_1(self):
        self.assertEqual("Hal", self.game_1.player_1.name)