import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(unittest.TestCase):
    
    def setUp(self):
        self.game_1 = Game(Player("Hal", "Rock"), Player("Dave", "Scissors"))

    def test_game_has_player_1(self):
        self.assertEqual("Hal", self.game_1.player_1.name)

    def test_game_has_player_2(self):
        self.assertEqual("Scissors", self.game_1.player_2.choice)