class Player:
    def __init__(self, name, input_choice):
        self.name = name
        self.input_choice = input_choice
        options = {
            "Rock" : 1,
            "Paper" : 2,
            "Scissors" : 3
        }
        self.choice = options[input_choice]
        