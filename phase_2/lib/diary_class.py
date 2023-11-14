class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.pos = 0

    def format(self):
        return f'{self.title} : {self.contents}'

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return len(self.contents.split())/wpm

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        wordsRead = wpm * minutes
        chunk = ' '.join(words[self.pos:self.pos + wordsRead])
        self.pos += wordsRead
        return chunk
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass