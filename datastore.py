import random
import sqlite3

class Datastore():
    
    def __init__(self):
        """
        intialise datastore by connecting to the sqlite db
        """
        db_file = "hangman_datastore.db"
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        
            
    def get_word(self):
        """
        returns a random word of 3 or more characters
        return: str
        """
        
        self.cur.execute(
            """
            SELECT word
            FROM Words
            """
        )
        results = self.cur.fetchall()
        return random.choice(results)[0]
        