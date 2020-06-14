from tinydb import TinyDB, Query

db = TinyDB("db.json")


def list_all_stopped_downloads():
    print(db.all())

