from tinydb import TinyDB, Query
import string
import random

db = TinyDB("db.json")


def id_generate():
    letters_and_digits = string.ascii_lowercase + string.digits
    return "".join((random.choice(letters_and_digits) for i in range(8)))


def list_all_stopped_downloads():
    print(db.all())


def save_session(url, destination, file_name, link_type):
    db.insert(
        {
            "id": id_generate(),
            "url": url,
            "file_name": file_name,
            "destination": destination,
            "link_type": link_type
        }
    )
