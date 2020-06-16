import click
from service import resume_downloader
from service.PyInquireTemplate import PyInquirerHandler


@click.group()
def resumeDownloadManager():
    pass


@resumeDownloadManager.command(help="List all stopped downloads")
def list_all_stopped_downloads():
    resume_downloader.list_all_stopped_downloads()


@resumeDownloadManager.command(help="Show the session information")
@click.argument("session-id")
def show_session_info(session_id):
    resume_downloader.show_session_info(session_id)


@resumeDownloadManager.command(help="Resume a stopped download")
@click.argument("session-id")
def resume_download(session_id):
    resume_downloader.resume_download(session_id)


@resumeDownloadManager.command(help="Delete existing session")
@click.option("--id", "-i", help="ID of the session")
def delete(id):
    if id:
        resume_downloader.delete_session(id)
    else:
        inquirer = PyInquirerHandler()
        questions = [
            {
                "type": "list",
                "name": "delete-all-or-not",
                "message": "Do you want to delete all sessions?",
                "choices": ["Yes", "No"]
            }
        ]

        delete_all_or_not_answer = inquirer.get_answer(questions)
        choice = delete_all_or_not_answer["delete-all-or-not"]

        if choice == "No":
            input_id_question = [
                {
                    "type": "input",
                    "name": "session-id-input",
                    "message": "Input Session ID"
                }
            ]

            input_id = inquirer.get_answer(input_id_question)["session-id-input"]
            resume_downloader.delete_session(input_id)

        elif choice == "Yes":
            resume_downloader.delete_all_sessions()
            print("Delete all sessions")

