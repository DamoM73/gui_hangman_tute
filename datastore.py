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
        return: (int,str)
        """
        
        self.cur.execute(
            """
            SELECT word_id, word
            FROM Words
            """
        )
        results = self.cur.fetchall()
        
        while True:
            word = random.choice(results)
            if len(word[1]) > 3:
                return word    
    
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
        
        try:
            return results[0]
        except:
            return None
        
    
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
    
    
    def get_all_usernames(self):
        """"
        Retrieves and returns all usernames
        return: [str]
        """
        # execute SQL command
        self.cur.execute(
            """
            SELECT name
            FROM Users
            """
        )
        # fetch results
        results = self.cur.fetchall()
        
        users = []
        
        for value in results:
            users.append(value[0])
        
        return users
    
    
    def get_guessed_words(self, user_id):
        """
        Retrieve a list of guessed words
        user_id: int
        return: [str]
        """
        self.cur.execute(
            """
            SELECT word
            FROM Words
            WHERE word_id IN (
                SELECT word_id
                FROM Games
                WHERE user_id = :user_id AND
                guessed = "TRUE"
            )
            """,
            {
                "user_id":user_id
            }
        )
        
        results = self.cur.fetchall()
        
        if results == []:
            return results
        else:
            words = []
            for value in results:
                words.append(value[0])
                
            return words
    
    
    def get_games_played(self,user_id):
        pass
    
    
    def get_games_won(self,user_id):
        pass
    
    
    def get_longest_word(self,user_id):
        pass
    
    
    def get_most_frequent(self,user_id):
        pass
    
    
    # add methods
    def add_credentials(self,user_name,password):
        """
        Insert username and password into datastore
        user_name: str
        password: str
        """
        # execute SQL command
        self.cur.execute(
            """
            INSERT INTO Users (name,password)
            VALUES (:name,:password)
            """,
            {
                "name":user_name,
                "password":password
            }
        )
        
        # commit command
        self.conn.commit()
        
    
    def add_result(self, user_id, word_id, guessed):
        """
        Adds game result to the games table
        user_id: int
        word_id: int
        guessed: str
        """
        self.cur.execute(
            """
            INSERT INTO Games (user_id, word_id, guessed)
            VALUES (:user_id,:word_id,:guessed)
            """,
            {
                "user_id":user_id,
                "word_id":word_id,
                "guessed":guessed
            }
        )
        
        self.conn.commit()