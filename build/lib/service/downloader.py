import requests
from tqdm import tqdm
from pySmartDL import SmartDL


def download_default(url):
    chunk_size = 1024
    req = requests.get(url, stream=True)

    total_size = int(req.headers['content-length'])

    with open("downloaded/download.pdf", 'wb') as file:
        for data in tqdm(iterable=req.iter_content(chunk_size), total=total_size / chunk_size, unit="KB"):
            file.write(data)


def download_smart(url, dest):
    obj = SmartDL(url, dest)
    obj.start(blocking=False)

    tqdm(iterable=obj.filesize, unit="KB")

    print("Downloaded file successfully to {}".format(obj.get_dest()))
