from pyfiglet import Figlet
from PyInquirer import style_from_dict, prompt, Token, Separator
from api import commands


def display_trademark():
    figlet = Figlet(font="speed")
    print(figlet.renderText("Stupid Downloader"))


def main():
    commands.downloadManager()


def draft():
    from service.DownloadFiles import DownloadFiles
    urls = [
        "http://quatest1.com.vn/images/PHP-DocumentFull.pdf",
        "http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf"
        "https://riptutorial.com/Download/node-js.pdf"
    ]
    destination = "downloaded"
    d = DownloadFiles(urls, destination)
    d.download()


if __name__ == "__main__":
    display_trademark()
    main()
