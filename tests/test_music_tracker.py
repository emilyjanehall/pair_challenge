from lib.music_tracker import *

def test_return_when_empty():
    music_tracker = MusicTracker()
    assert music_tracker.list_tracks() == []

def test_add_valid_track():
    music_tracker = MusicTracker()
    music_tracker.add_track("Snow")
    assert music_tracker.list_tracks() == ["Snow"]