class Room:

    def __init__(self, name, till, capacity):
        self.name = name
        self.till = till
        self.capacity = capacity
        self.list_of_guests = []
        self.play_list = []

    def check_in_guest(self, guest):
        self.list_of_guests.append(guest)

    def check_out_guest(self, guest):
        self.list_of_guests.remove(guest)

    def pay_entry_fee(self, money):
        self.till += money

    def add_song(self, song):
        self.play_list.append(song)

    def no_more_guests(self, guest):
        if len(self.list_of_guests) > self.capacity:
            self.list_of_guests.remove(guest)
        else:
            self.list_of_guests.append(guest)

    

    


    