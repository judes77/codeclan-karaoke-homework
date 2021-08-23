class Guest:
    
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def can_pay_room(self, room):
        self.wallet -= room.till