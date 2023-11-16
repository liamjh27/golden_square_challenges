class Music:
    def __init__(self):
        self.listened_to = []

    def add(self, artist, song):
        self.listened_to.append(f'{artist} - {song}')

    def show(self):
        return self.listened_to