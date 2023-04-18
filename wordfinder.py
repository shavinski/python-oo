import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_destination):
        """Creates instance with a assigned file destination"""
        self.file_destination = file_destination
        self.words = list(open(self.file_destination))
        self.print_words_read()
        #print(f"{len(self.words)} words read")
        
    def __repr__(self):
        return f"<Words read from {self.file_destination}"

    def print_words_read(self):
        """On first instantiation it will print num of words in file"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Prints random word from file_destination"""
    
        #words = list(open(self.file_destination))
        words_sliced = []

        for word in self.words:
            if word.endswith('\n'):
                words_sliced.append(word[:-1:])
            else:
                words_sliced.append(word)
    
        return random.choice(words_sliced)
    
word = WordFinder('random.txt')
word.random()
    







    
