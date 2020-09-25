class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def play(self):
        result = ((self.player_1.choice - self.player_2.choice) + 5 ) % 3 
        
        if result == 0:
            return f"{self.player_1.name} is the winner with {self.player_1.input_choice}!"
        elif result == 1:
            return f"{self.player_2.name} is the winner with {self.player_2.input_choice}!"
        else:
            return "It's a draw!"