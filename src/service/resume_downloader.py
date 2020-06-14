from tinydb import TinyDB, Query
from tabulate import tabulate
import string
import random

db = TinyDB("db.json")


def id_generate():
    letters_and_digits = string.ascii_lowercase + string.digits
    return "".join((random.choice(letters_and_digits) for i in range(8)))


def list_all_stopped_downloads():
    sessions = db.all()

    table_headers = ["ID", "File name", "Link type"]
    rows = []

    for session in sessions:
        id = session["id"]
        url = session["url"]
        file_name = session["file_name"]
        destination = session["destination"]
        link_type = session["link_type"]

        rows.append([id, file_name, link_type])

    print(tabulate(rows, table_headers, tablefmt="orgtbl"))



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
