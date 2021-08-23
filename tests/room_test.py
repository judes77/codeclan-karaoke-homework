import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Harmony", 5, 4)
        self.guest_1 = Guest("Callum", 39, 80)
        self.guest_2 = Guest("Rob", 40, 100)
        self.guest_3 = Guest("Mark", 41, 90)
        self.guest_4 = Guest("Sean", 39, 100)
        self.guest_5 = Guest("Craig", 41, 120)
        self.song_1 = Song("Living on a Prayer", "Bon Jovi")
        

    def test_room_has_name(self):
        self.assertEqual("Harmony", self.room1.name)

    def test_room_has_price(self):
        self.assertEqual(5, self.room1.till)

    def test_room_has_capicity_number(self):
        self.assertEqual(4, self.room1.capacity)

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room1.list_of_guests))

    def test_check_out_guest(self):
        self.room1.check_in_guest(self.guest_1)
        self.room1.check_out_guest(self.guest_1)
        self.assertEqual(0, len(self.room1.list_of_guests))

    def test_add_song(self):
        self.room1.add_song(self.song_1)
        self.assertEqual(1, len(self.room1.play_list))

    def test_too_many_guests_checking(self):
        self.room1.list_of_guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5]
        self.room1.no_more_guests(self.guest_5)
        self.assertEqual(4, len(self.room1.list_of_guests))
    
    