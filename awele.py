class Awele:
    def __init__(self):
        self.plateau_up = {"A":4, "B":4, "C":4,
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
    
    def is_empty(self):
        for value in self.plateau_up.values():
            if value != 0:
                return False
        for value in self.plateau_down.values():
            if value != 0:
                return False
        return True
    
    def saw_process(self, start_key, number, dict_list_1, dict_list_2):
        start = False
        temp_dict_list_1 = dict_list_1
        temp_dict_list_2 = dict_list_2
        if "A" in dict_list_1:
            temp_dict_list_1 = dict(sorted(dict_list_1.items(),  reverse = True))
        else:
            temp_dict_list_2 = dict(sorted(dict_list_2.items(),  reverse = True))
        if start_key in temp_dict_list_1.keys():
            for key in temp_dict_list_1.keys():
                if key == start_key:
                    start = True
                if start and (number > 0):
                    dict_list_1[key] += 1
                    number -= 1
            if number > 0:
                for key in temp_dict_list_2.keys():
                    if (number > 0):
                        dict_list_2[key] += 1
                        number -= 1

    def saw(self, start_key, number):
        if start_key in self.plateau_up.keys():
            self.saw_process(start_key, number, self.plateau_up, self.plateau_down)
        elif start_key in self.plateau_down.keys():
            self.saw_process(start_key, number, self.plateau_down,self.plateau_up)

    def harvest_process(self, start_key, dict_list):
        start = False
        recolted_seed = 0
        temp_dict_list = dict_list
        if "A" in dict_list:
            temp_dict_list = dict(sorted(dict_list.items(),  reverse = True))

        if start_key in temp_dict_list.keys():
            for key in temp_dict_list.keys():
                if key == start_key:
                    start = True
                if start:
                    recolted_seed += dict_list[key]
                    dict_list[key] = 0
            return recolted_seed
        return 0

    def harvest(self, start_key):
        if start_key in self.plateau_up.keys():
            return self.harvest_process(start_key, self.plateau_up)
        elif start_key in self.plateau_down.keys():
            return self.harvest_process(start_key, self.plateau_down)
        return 0
            