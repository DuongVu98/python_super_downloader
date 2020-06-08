import click
from service import downloader


@click.group()
def downloadManager():
    pass


@downloadManager.command()
@click.argument("url")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download(url, destination, name):
    downloader.download_default(url, destination, name)


@downloadManager.command()
@click.argument("url")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download_separated_partitial(url, destination, name):
    downloader.download_separated_threads(url, destination, name)


@downloadManager.command()
def download_multi_files():
    print("hello")

    from service.PyInquireTemplate import PyInquirerHandler
    inquirer = PyInquirerHandler()
    questions = [
        {
            "type": "input",
            "name": "input1",
            "message": "Input the URL: "
        },
        {
            "type": "input",
            "name": "input2",
            "message": "Input the URL: "
        }
    ]
    answers = inquirer.get_answer(questions)
    print(answers)
    urls = []
    for input, url in answers.items():
        urls.append(url)

    downloader.download_multithreading(urls, "downloaded")
