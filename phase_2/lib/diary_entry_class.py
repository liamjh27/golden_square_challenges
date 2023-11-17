import re 

number_pattern = r'\b(07\d{9})\b'

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.pos = 0
        self.contains_number = False
        number = re.search(number_pattern, self.contents)
        if number:
            self.contains_number = True 
            self.num = number.group()


    def format(self):
        return f'{self.title} : {self.contents}'

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return len(self.contents.split())/wpm

    def reading_chunk(self, wpm, minutes):
        if self.pos >= self.count_words():
            self.pos = 0
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