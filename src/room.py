class Room:

    def __init__(self, name, price, capacity):
        self.name = name
        self.till = price
        self.capacity = capacity
        self.list_of_guests = []

    def check_in_guest(self, guest):
        self.list_of_guests.append(guest)

    