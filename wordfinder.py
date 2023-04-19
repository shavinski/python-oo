import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_destination):
        """Creates instance with a assigned file destination"""
        self.file_destination = open(file_destination)
        self.words = self.words_strip()
        self.print_words_read()

    def __repr__(self):
        return f"<Words read from {self.file_destination}>"

    def words_strip(self):
        "Removes white space from file"
        return [line.strip() for line in self.file_destination]

    def print_words_read(self):
        """On instantiation it will print num of words in file"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Prints random word from file_destination"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Adds extra conditions to WordFinder.words_strip"""
    def words_strip(self):
        return [word for word in super().words_strip() if word != "" and not
                word.startswith("#")]