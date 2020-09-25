import unittest
from player import Player

class PlayerTest(unittest.TestCase)

def setUp(self):
    player_1 = Player("Hal", "Rock")
    player_2 = Player("Dave", "Scissors")

def test_player_has_name(self):
    self.assertEqual("Hal", player_1.name)