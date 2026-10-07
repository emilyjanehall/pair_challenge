```python
#As a user
#So that I can keep track of my music listening
#I want to add tracks I've listened to and see a list of them.

class MusicTracker:
    def __init__(self):
        self.track_list = []

    def add_track(self, track_name):
        # Adds track name to list

    def list_tracks(self):
        # Returns self.track_list

"""
Given an empty list
track_list returns an empty list
"""
music_tracker = MusicTracker()
music_tracker.list_tracks() # => []

"""
Given a track name
Adds track to track_list
"""
music_tracker = MusicTracker()
music_tracker.add_track("Song")
music_tracker.list_tracks() # => ["Song"]

"""
Given an invalid data type
Raises TypeError
"""
music_tracker = MusicTracker()
music_tracker.add_track(1) # => raises Exception "Invalid data type"
```