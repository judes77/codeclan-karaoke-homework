import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Harmony", 5, 8)
        self.guest_1 = Guest("Callum", 39, 80)


        
    def test_room_has_name(self):
        self.assertEqual("Narnia", self.room.name)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room.list_of_guests))

    