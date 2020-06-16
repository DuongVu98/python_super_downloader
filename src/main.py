from pyfiglet import Figlet
from api import commands, resume_commands, cli


def display_trademark():
    figlet = Figlet(font="speed")
    print(figlet.renderText("Netprog Stupid Downloader"))


def download_commands():
    commands.downloadManager()


def resume_download_commands():
    resume_commands.resumeDownloadManager()


if __name__ == "__main__":
    display_trademark()
    cli.cli()
