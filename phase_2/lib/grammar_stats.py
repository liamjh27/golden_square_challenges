class GrammarStats:
    def __init__(self):
        self.tests = 0
        self.passed = 0
  
    def check(self, text):
        self.tests += 1
        if text[0].isupper() and text[-1] in '.!?':
            self.passed += 1
            return True
        return False

        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
  
    def percentage_good(self):
        return (self.passed/self.tests)*100
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.