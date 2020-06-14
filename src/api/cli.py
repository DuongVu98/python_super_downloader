import click

from api.commands import downloadManager
from api.resume_commands import resumeDownloadManager

cli = click.CommandCollection(sources=[
    downloadManager,
    resumeDownloadManager
])