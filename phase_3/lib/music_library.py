class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)
    def search(self, keyword):
        return list(filter(lambda track: track.matches(keyword), self.tracks))