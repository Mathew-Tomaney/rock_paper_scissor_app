class Player:
    def __init__(self, name, choice):
        self.name = name
        options = {
            "Rock" : 1,
            "Paper" : 2,
            "Scissors" : 3
        }
        self.choice = options[choice]
        