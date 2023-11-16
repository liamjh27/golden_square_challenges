class Diary():
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

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