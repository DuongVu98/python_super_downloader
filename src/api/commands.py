import click
from service import downloader


@click.group()
def downloadManager():
    pass


@downloadManager.command()
@click.argument("url")
@click.option("--destination","-d", default="downloaded",show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download(url, destination, name):
    downloader.download_default(url, destination, name)


@downloadManager.command()
@click.argument("url")
@click.option("--destination","-d", default="downloaded",show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download_separated_threads(url, destination, name):
    downloader.download_separated_threads(url, destination, name)
