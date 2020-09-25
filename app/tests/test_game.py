import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(unittest.TestCase):
    
    def setUp(self):
        self.game_1 = Game(Player("Hal", "Rock"), Player("Dave", "Scissors"))
        self.game_2 = Game(Player("Rick", "Rock"), Player("Morty", "Scissors"))
        self.game_3 = Game(Player("Bill", "Paper"), Player("Ted", "Paper"))
        self.game_4 = Game(Player("Merry", "Rock"), Player("Pippin", "Paper"))


    def test_game_has_player_1(self):
        self.assertEqual("Hal", self.game_1.player_1.name)

    def test_game_has_player_2(self):
        self.assertEqual(3, self.game_1.player_2.choice)


    def test_game_can_play__player_1_win(self):
        self.assertEqual("Rick is the winner with Rock!", self.game_2.play())
    
    def test_game_can_play__player_2_win(self):
        self.assertEqual("Pippin is the winner with Paper!", self.game_4.play())
    
    def test_game_can_play__tied_game(self):
        self.assertEqual("It's a draw!", self.game_3.play())

    
