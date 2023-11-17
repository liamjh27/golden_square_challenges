class Diary():
    def __init__(self):
        self.entries = []
        self.phone_numbers = []

    def add(self, entry):
        self.entries.append(entry)
        if entry.contains_number:
            self.phone_numbers.append(entry.num)

    def all(self):
        return self.entries

    def count_words_total(self):
        return sum([entry.count_words() for entry in self.entries])

    def reading_time(self, wpm):
        return sum([entry.reading_time(wpm) for entry in self.entries])

    def best_entry_for_reading_time(self, wpm, time):
        max_length = wpm * time
        entries_word_count = {}
        for entry in self.entries:
            if entry.count_words() <= max_length:
                entries_word_count[entry] = entry.count_words()
        # print(entries_word_count)
        best_match = sorted(entries_word_count.items(), key=lambda item: item[1])[-1][0]
        return best_match

    def read(self, entry):
        return entry.format()    


    def get_numbers(self):
        return self.phone_numbers 