from datastore import Datastore

db = Datastore()

print(db.get_guessed_words(2))