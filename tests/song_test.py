import unittest

from src.song import Song
from src.room import Room

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Living on a Prayer", "Bon Jovi")

    def test_song_has_title(self):
        self.assertEqual("Living on a Prayer", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Bon Jovi", self.song_1.artist)

    
