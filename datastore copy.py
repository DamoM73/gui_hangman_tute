import random

class Datastore():
    
    def __init__(self):
        """
        intialise datastore by reading dictionary file and 
        adding each word into a list
        """
        with open("dictionary.txt","r") as word_file:
            self.words = word_file.read().splitlines()
            
    def get_word(self):
        """
        returns a random word of 3 or more characters
        return: str
        """
        word = ""
        while len(word) < 3:
            word = random.choice(self.words)
            
        return word