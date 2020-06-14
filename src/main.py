from pyfiglet import Figlet
from api import commands


def display_trademark():
    figlet = Figlet(font="speed")
    print(figlet.renderText("Netprog Stupid Downloader"))


def main():
    commands.downloadManager()


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

    import requests
    r = requests.get("http://www.mediafire.com/file/0rdnw9gw2g6vdo7/1HCR12.pdf/file")
    # print(r.text)

    import re
    result = re.findall('<a\s[^<]*href="(.*)">\s*Download', r.text)
    print(result)


if __name__ == "__main__":
    display_trademark()
    main()
