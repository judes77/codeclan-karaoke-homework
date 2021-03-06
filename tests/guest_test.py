import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Callum", 39, 80)
        self.room1 = Room ("Manic", 10, 6)

    def test_guest_has_name(self):
        self.assertEqual("Callum", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(39, self.guest_1.age)

    def test_guest_has_wallet(self):
        self.assertEqual(80, self.guest_1.wallet)

    def test_guest_can_pay_room(self):
        self.guest_1.can_pay_room(self.room1)
        self.assertEqual(70, self.guest_1.wallet)

        