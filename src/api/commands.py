import click
from service import downloader
import os


@click.group()
def downloadManager():
    pass


@downloadManager.command()
@click.argument("url")
def download(url):
    downloader.download_default(url)


@downloadManager.command()
@click.argument("url")
@click.option("--dest", "-d", default=os.getcwd(), help="destination to download")
def download_smart(url, dest):
    downloader.download_smart(url, dest)
