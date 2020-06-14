from tinydb import TinyDB, Query
from tabulate import tabulate
from tqdm import tqdm
import string
import random
import requests
import os

db = TinyDB("db.json")
query = Query()


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


def resume_download(session_id):
    result = db.search(query.id == session_id)

    if result[0] is None:
        print("There is no session with ID {}".format(session_id))
    else:
        session = result[0]
        url = session["url"]
        file_name = session["file_name"]
        destination = session["destination"]
        link_type = session["link_type"]

        full_file_name = "{}/{}".format(destination, file_name)
        size = os.path.getsize(full_file_name)

        if link_type == "direct":
            headers = {"Range": "bytes={}-".format(size)}
            r = requests.get(url, stream=True, headers=headers)
            total_size = int(r.headers.get('content-length', 0))
            block_size = 1024
            t = tqdm(total=total_size, unit='iB', unit_scale=True)
            with open(full_file_name, 'ab') as f:
                for data in r.iter_content(block_size):
                    t.update(len(data))
                    f.write(data)
            t.close()

    db.remove(query.id == session_id)