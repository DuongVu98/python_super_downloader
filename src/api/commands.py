import click
from service import downloader
from service import resume_downloader
from service.PyInquireTemplate import PyInquirerHandler


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
        print("Downloading session saved")
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
    print("hello")

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
    print(answers)

    urls = []
    for index, key in enumerate(answers):
        if index >= 1:
            urls.append(answers[key])

    if answers["method_selection"] == "Multi-Threading":
        downloader.download_multifiles_parallelly(urls, destination)
    else:
        downloader.download_multifiles_concurrently(urls, destination)


def make_single_question(i):
    return {
        "type": "input",
        "name": "input{}".format(i),
        "message": "Input the URL {}: ".format(i)
    }


@downloadManager.command(help="Download file from MediaFire")
@click.option("--url", "-u", help="mediafire link for downloading")
@click.option("--destination", "-d", default="downloaded", show_default=True, help="destination to save file")
@click.option("--name", "-n", help="rename file")
def download_from_mediafire(url, destination, name):
    if url is not None:
        downloader.download_file_from_mediafire(url, destination, name)
    else:
        inquirer = PyInquirerHandler()
        questions = [
            {
                "type": "list",
                "name": "single-or-multi-question",
                "message": "Do you want to download from single or multiple MediaFire links?: ",
                "choices": ["Single link", "Multiple links"]
            }
        ]

        single_or_multi_answer = inquirer.get_answer(questions)
        choice = single_or_multi_answer["single-or-multi-question"]
        if choice == "Single link":
            single_file_question = [
                {
                    "type": "input",
                    "name": "mediafire-link-input",
                    "message": "Input MediaFire link"
                }
            ]
            mediafire_link_answer = inquirer.get_answer(single_file_question)
            downloader.download_file_from_mediafire(mediafire_link_answer["mediafire-link-input"], destination, name)
        elif choice == "Multiple links":
            number_of_links_questions = [
                {
                    "type": "input",
                    "name": "number-of-links",
                    "message": "Number of MediaFire links: "
                }
            ]
            number_of_links_answer = inquirer.get_answer(number_of_links_questions)

            input_links_questions = []
            for i in range(1, int(number_of_links_answer["number-of-links"]) + 1):
                input_links_questions.append(make_single_question(i))
            input_links_answers = inquirer.get_answer(input_links_questions)

            urls = []
            for index, key in enumerate(input_links_answers):
                urls.append(input_links_answers[key])

            method_question = [
                {
                    "type": "list",
                    "name": "method_question",
                    "message": "Input the method to download",
                    "choices": [
                        "Multi-Threading",
                        "Multi-Processing"
                    ]
                }
            ]
            method_answer = inquirer.get_answer(method_question)
            downloader.download_multiple_files_from_mediafire(urls, destination, method=method_answer["method_question"])
