class Room:

    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.list_of_guests = []
        self.play_list = []

    def check_in_guest(self, guest):
        self.list_of_guests.append(guest)

    def check_out_guest(self, guest):
        self.list_of_guests.remove(guest)

    def add_song(self, song):
        self.play_list.append(song)

    