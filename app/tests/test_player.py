import unittest
from app.models.player import Player

class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Hal", "Rock")
        self.player_2 = Player("Dave", "Scissors")

    def test_player_has_name(self):
        self.assertEqual("Hal", self.player_1.name)

    def test_player_has_choice(self):
        self.assertEqual("Scissors", self.player_2.choice)