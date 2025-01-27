class Awele:
    def __init__(self):
        self.plateau_up = {"A":0, "B":0, "C":0,
                           "D":0, "E":0,  "F":0}
        self.plateau_down = {"G":0,  "H":0, "I":0,
                             "J":0,  "K":0,  "L":0}
        
    def display_key(self, lis_key:list):
        key_string = " "
        i = 0
        for key in lis_key:
            if (i > 0):
                key_string += "  "
            key_string += key
            i = i + 1
        print(key_string)

    def display_value(self, lis_value:list):
        value_string = ""
        for value in lis_value:
            value_string += "("
            value_string += str(value)
            value_string += ")"
        print(value_string)

    def display(self):
        self.display_key(self.plateau_up.keys())
        self.display_value(self.plateau_up.values())
        self.display_value(self.plateau_down.values())
        self.display_key(self.plateau_down.keys())
        
        
if __name__ == '__main__':
    game = Awele()
    game.display()