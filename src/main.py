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
    pass


if __name__ == "__main__":
    display_trademark()
    cli.cli()
    # draft()
