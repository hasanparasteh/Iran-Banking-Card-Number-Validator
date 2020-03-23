import math

class BankingCardValidator:
    def __init__(self):
        pass

    def set_card_number(self, card_number):
        self.card_number = int(card_number)
    
    def get_card_number(self):
        return self.card_number
    
    def seprate_card_number(self):
        return [int(x) for x in str(self.card_number)]
    
    def calculate_card_number_length(self):
        if(self.card_number != None):
            return int(math.log10(self.card_number)) + 1
    
    def multipy(self, number):
        if(number % 2 == 0):
            return number * 1
        else:
            return number * 2

    def loop_calculations(self, numbers_array):
        answer = 0
        final = 0
        for number in numbers_array:
            answer = self.multipy(number)
            if(answer > 9):
                answer = answer - 9
            final += answer
        return final

    def is_length_valid(self):
        if(16 == self.calculate_card_number_length()):
            return True
        else:
            return False
    
    def is_card_valid(self):
        if(not self.is_length_valid()):
            return False
    
        card_number_arr = self.seprate_card_number() # converts card number into array
        if(self.loop_calculations(card_number_arr) % 10 == 0):
            return True
        else:
            return False
