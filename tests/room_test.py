import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Harmony", 5, 8)
        self.guest_1 = Guest("Callum", 39, 80)
        self.song_1 = Song("Living on a Prayer", "Bon Jovi")


    def test_room_has_name(self):
        self.assertEqual("Harmony", self.room.name)

    def test_room_has_price(self):
        self.assertEqual(5, self.room.price)

    def test_room_has_capicity_number(self):
        self.assertEqual(8, self.room.capacity)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room.list_of_guests))

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, len(self.room.list_of_guests))

    def test_add_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, len(self.room.play_list))

    