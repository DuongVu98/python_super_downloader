import click
from service import downloader
import threading


@click.group()
def downloadManager():
    pass


@downloadManager.command(help="Download file with single thread")
@click.argument("url")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download(url, destination, name):
    downloader.download_default(url, destination, name)


@downloadManager.command(help="Download file with separated parts")
@click.argument("url")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download_separated_parts(url, destination, name):
    downloader.download_separated_threads(url, destination, name)


@downloadManager.command(help="Download file with multiple threads")
@click.option("--number-of-files", "-n", prompt="Number of files ? ")
def download_multi_files(number_of_files):
    print("hello")

    from service.PyInquireTemplate import PyInquirerHandler
    inquirer = PyInquirerHandler()
    questions = []
    for i in range(1, int(number_of_files) + 1):
        questions.append(make_single_question(i))
    answers = inquirer.get_answer(questions)
    print(answers)
    urls = []
    for input, url in answers.items():
        urls.append(url)

    # downloader.download_multithreading(urls, "downloaded")
    for i, url in enumerate(urls):
        print("print the i --> {}".format(i))
        thread = threading.Thread(target=downloader.download_single_thread, kwargs={
            "url": url,
            "destination": "downloaded",
            "progress_bar_position": i
        })
        # thread.setDaemon(True)
        thread.start()


def make_single_question(i):
    return {
        "type": "input",
        "name": "input{}".format(i),
        "message": "Input the URL {}: ".format(i)
    }
