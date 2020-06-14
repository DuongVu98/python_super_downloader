import click


@click.group()
def resumeDownloadManager():
    pass


@resumeDownloadManager.command(help="List all stopped downloads")
def list_all_stopped_downloads():
    pass


@resumeDownloadManager.command(help="Resume a stopped download")
@click.argument("session-id")
def resume_download(session_id):
    pass
