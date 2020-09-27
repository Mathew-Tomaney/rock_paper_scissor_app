import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(unittest.TestCase):
    
    def setUp(self):
        self.game_1 = Game(Player("Hal", "Rock"), Player("Dave", "Scissors"))
        self.game_2 = Game(Player("Rick", "Rock"), Player("Morty", "Scissors"))
        self.game_3 = Game(Player("Bill", "Paper"), Player("Ted", "Paper"))
        self.game_4 = Game(Player("Merry", "Rock"), Player("Pippin", "Paper"))
        self.game_5 = Game(Player("Bob", "Rock"), )


    def test_game_has_player_1(self):
        self.assertEqual("Hal", self.game_1.player_1.name)

    def test_game_has_player_2(self):
        self.assertEqual(3, self.game_1.player_2.choice)


    def test_game_can_play__player_1_win(self):
        self.assertEqual("Rick", self.game_2.play().name)
    
    def test_game_can_play__player_2_win(self):
        self.assertEqual("Paper", self.game_4.play().input_choice)
    
    def test_game_can_play__tied_game(self):
        self.assertEqual(None, self.game_3.play())

    def test_show_results__winner(self):
        self.game_1.play()
        self.assertEqual("Hal wins by playing Rock!", self.game_1.show_results())

    def test_show_results__draw(self):
        self.game_3.play()
        self.assertEqual("It's a draw!", self.game_3.show_results())

    def test_game_gets_computer_player(self):
        self.assertEqual("Computer", self.game_5.player_2.name)
