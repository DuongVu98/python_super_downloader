import click
from service import downloader
from service import resume_downloader


@click.group()
def downloadManager():
    pass


@downloadManager.command(help="Download file with single thread")
@click.argument("url")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download(url, destination, name):
    if name is None:
        name = url.split('/')[-1]
    try:
        downloader.download_default(url, destination, name)
    except KeyboardInterrupt:
        resume_downloader.save_session(url, destination=destination, file_name=name, link_type="direct")


@downloadManager.command(help="Download file with separated parts")
@click.argument("url")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download_separated_parts(url, destination, name):
    downloader.download_separated_threads(url, destination, name)


@downloadManager.command(help="Download file with multiple threads")
@click.option("--number-of-files", "-n", prompt="Number of files ? ", help="Number of files")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
def download_multi_files(number_of_files, destination):
    start_download = False
    try:
        from service.PyInquireTemplate import PyInquirerHandler
        inquirer = PyInquirerHandler()
        questions = [
            {
                "type": "list",
                "name": "method_selection",
                "message": "Choose the method: ",
                "choices": [
                    "Multi-Threading",
                    "Multi-Processing"
                ]
            }
        ]

        for i in range(1, int(number_of_files) + 1):
            questions.append(make_single_question(i))
        answers = inquirer.get_answer(questions)

        urls = []
        for index, key in enumerate(answers):
            if index >= 1:
                urls.append(answers[key])

        if answers["method_selection"] == "Multi-Threading":
            start_download = True
            downloader.download_multifiles_in_parallel(urls, destination)
        else:
            start_download = True
            downloader.download_multifiles_in_concurrency(urls, destination)

    except KeyboardInterrupt:
        print("stop")
        if start_download:
            for url in urls:
                file_name = url.split('/')[-1]
                resume_downloader.save_session(url, destination=destination, file_name=file_name, link_type="direct")


def make_single_question(i):
    return {
        "type": "input",
        "name": "input{}".format(i),
        "message": "Input the URL {}: ".format(i)
    }


@downloadManager.command(help="Download file from MediaFire")
@click.argument("url")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download_from_mediafire(url, destination, name):
    downloader.download_file_from_mediafire(url, destination, name)
