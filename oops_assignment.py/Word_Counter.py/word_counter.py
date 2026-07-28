import string

class WordProcessor:
    def __init__(self, text):
        # Composition: class is composed of text storage + counting + analyzing
        self.words = text   # uses setter for validation

    # Copy constructor 
    def __init_copy__(self, other):
        self._words = other._words.copy()

    # Encapsulation with property + setter + validation 
    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, text):
        if isinstance(text, WordProcessor):         # copy constructor case
            self._words = text._words.copy()
        elif isinstance(text, str):                 # if string, split into words
            self._words = text.split()
        elif isinstance(text, list):                # if list, store directly
            self._words = text
        else:
            raise TypeError("WordProcessor accepts string, list, or WordProcessor")

    def count(self):
        freq = {}
        for word in self._words:
            clean_word = word.lower().strip(string.punctuation)
            if clean_word:   # skip empty strings
                freq[clean_word] = freq.get(clean_word, 0) + 1
        return freq

    def analyze(self):
        return self.count()

    def display(self):
        print("\nWord frequencies:")
        for word, count in self.analyze().items():
            print(f"{word}: {count}")









