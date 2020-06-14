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

    import urllib.request
    # headers = {"Range": "bytes={}-{}".format(0, 1000)}
    # downloadRequest = urllib.request.Request(url="http://quatest1.com.vn/images/PHP-DocumentFull.pdf", headers=headers)
    # with urllib.request.urlopen(downloadRequest) as response, open("downloaded/resumetest.pdf", 'wb') as out_file:
    #     data = response.read()  # a `bytes` object
    #     out_file.write(data)

    # headers = {"Range": "bytes={}-".format(1000)}
    # downloadRequest = urllib.request.Request(url="http://quatest1.com.vn/images/PHP-DocumentFull.pdf", headers=headers)
    # with urllib.request.urlopen(downloadRequest) as response, open("downloaded/resumetest.pdf", 'ab') as out_file:
    #     data = response.read()  # a `bytes` object
    #     out_file.write(data)

    opener = urllib.request.build_opener()
    opener.addheaders = [('Range', 'bytes={}-'.format(1000))]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve("type URL here", "path/file_name")


if __name__ == "__main__":
    display_trademark()
    cli.cli()
