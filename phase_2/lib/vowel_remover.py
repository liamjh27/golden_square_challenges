
class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        new_string = ''
        for char in self.text:
            if char in self.vowels:
                new_string = new_string
            else:
                new_string += char
        self.text = new_string
        return self.text


