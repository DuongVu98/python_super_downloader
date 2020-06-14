import click
from service import resume_downloader


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
