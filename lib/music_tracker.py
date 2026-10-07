class MusicTracker():
    def __init__(self):
        self.track_list = []

    def list_tracks(self):
        return self.track_list

    def add_track(self, name):
        self.track_list.append(name)