
class Playeur:
    def __init__(self, plateau):
        self.plateau = plateau
        self.handle_seed = 0
        self.score = 0
    
    def increment_score(self, number):
        self.score += number
