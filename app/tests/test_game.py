import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(unittest.TestCase):
    
    def setUp(self):
        self.game_1 = Game(Player("Hal", 1), Player("Dave", 3))
        self.game_2 = Game(Player("Rick", 1), Player("Morty", 3))
        self.game_3 = Game(Player("Bill", 2), Player("Ted", 2))
        self.game_4 = Game(Player("Merry", 1), Player("Pippin", 2))


    def test_game_has_player_1(self):
        self.assertEqual("Hal", self.game_1.player_1.name)

    def test_game_has_player_2(self):
        self.assertEqual(3, self.game_1.player_2.choice)


    def test_game_can_play__player_1_win(self):
        self.assertEqual("Rick is the winner with 1!", self.game_2.play())
    
    def test_game_can_play__player_2_win(self):
        self.assertEqual("Pippin is the winner with 2!", self.game_4.play())
    
    def test_game_can_play__tied_game(self):
        self.assertEqual("It's a draw!", self.game_3.play())

    
