class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winning_player = None


    def play(self):
        result = ((self.player_1.choice - self.player_2.choice) + 5 ) % 3 
        
        if result == 0:
            self.winning_player = self.player_1
        elif result == 1:
            self.winning_player = self.player_2
        return self.winning_player