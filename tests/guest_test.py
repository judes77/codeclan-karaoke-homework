import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Callum", 39, 80)

    def test_guest_has_name(self):
        self.assertEqual("Callum", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(39, self.guest_1.age)

        