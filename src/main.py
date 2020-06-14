from pyfiglet import Figlet
from api import commands, resume_commands, cli


def display_trademark():
    figlet = Figlet(font="speed")
    print(figlet.renderText("Netprog Stupid Downloader"))


def download_commands():
    commands.downloadManager()


def resume_download_commands():
    resume_commands.resumeDownloadManager()


def draft():
    # from service.DownloadFilesConcurrently import DownloadFilesConcurently
    # urls = [
    #     "http://quatest1.com.vn/images/PHP-DocumentFull.pdf",
    #     "http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf"
    #     "https://riptutorial.com/Download/node-js.pdf"
    # ]
    # destination = "downloaded"
    # d = DownloadFilesConcurently(urls, destination)
    # d.download()

    # import os
    # size = os.path.getsize("downloaded/PHP-DocumentFull.pdf")

    # import urllib.request
    # headers = {"Range": "bytes={}-{}".format(0, 45000)}
    # downloadRequest = urllib.request.Request(url="http://quatest1.com.vn/images/PHP-DocumentFull.pdf", headers=headers)
    # with urllib.request.urlopen(downloadRequest) as response, open("downloaded/resumetest.pdf", 'wb') as out_file:
    #     data = response.read()  # a `bytes` object
    #     out_file.write(data)

    # import requests
    # from tqdm import tqdm
    #
    # headers = {"Range": "bytes={}-".format(45000)}
    # url = "http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf"
    # r = requests.get(url, stream=True, headers=headers)
    # total_size = int(r.headers.get('content-length', 0))
    # block_size = 1024
    # t = tqdm(total=total_size, unit='iB', unit_scale=True)
    # with open('downloaded/resumetest.pdf', 'ab') as f:
    #     for data in r.iter_content(block_size):
    #         t.update(len(data))
    #         f.write(data)
    # t.close()

    from tinydb import TinyDB, Query
    import string, random
    db = TinyDB("db.json")
    lettersAndDigits = string.ascii_lowercase + string.digits
    db.insert(
        {
            "id": ''.join((random.choice(lettersAndDigits) for i in range(8))),
            "url": "blah",
            "stopPos": 123,
            "fileName": "blahblah"
        }
    )


if __name__ == "__main__":
    display_trademark()
    # cli.cli()
    draft()
