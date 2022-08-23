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
    
    def __del__(self):
        self.conn.close()
    
    
    # get methods        
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
        
        while True:
            word = random.choice(results)[0]
            if len(word) > 3:
                return word
            
    
    # get methods
    def get_password(self,user):
        """
        Retrieves user's password
        user: str
        return: str
        """
        
        self.cur.execute(
            """
            SELECT password
            FROM Users
            WHERE name = :user
            """,
            {
                "user":user
            }
        )
        results = self.cur.fetchone()
        if results is None:
            return None
        else:
            return results[0]
        
    
    def get_user_id(self, user):
        """
        Returns the user_id for the provided user
        user: str
        return: int
        """
        self.cur.execute(
            """
            SELECT user_id
            FROM Users
            WHERE name = :name
            """,
            {
                "name":user
            }
        )
        
        results = self.cur.fetchone()[0]
        
        return results
        
    # add methods