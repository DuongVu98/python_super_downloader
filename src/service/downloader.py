import urllib.request
import threading

from service.MediaFireDownload import MediaFireDownload, MultiMediaFireDownload
from service.ProgressBar import ProgressBar
from service.ThreadedFetch import ThreadedFetch
from service.DownloadMultiFiles import DownloadFilesParallelly, DownloadFilesConcurrently


def download_default(url, destination, file_name):
    if file_name is None:
        file_name = url.split('/')[-1]

    with ProgressBar(unit='B', unit_scale=True, miniters=1, desc=file_name) as t:
        urllib.request.urlretrieve(url, filename="{}/{}".format(destination, file_name), reporthook=t.update_to)


def download_separated_threads(url, destination, file_name):
    dl = ThreadedFetch(url, file_name)
    dl.start()
    dl.join()
    content = dl.get_file_data()
    if content:
        with open("{}/{}".format(destination, file_name), 'w') as fh:
            fh.write(str(content))
        print("Finished Writing file %s" % file_name)


def download_single_thread(url, destination, progress_bar_position):
    file_name = url.split('/')[-1]

    with ProgressBar(unit='B', unit_scale=True, miniters=1, desc=file_name,
                     position=progress_bar_position) as t:
        urllib.request.urlretrieve(url, filename="{}/{}".format(destination, file_name), reporthook=t.update_to)


def download_multifiles_in_parallel(urls, destination):
    parallel = DownloadFilesParallelly(urls, destination)
    parallel.download()


def download_multifiles_in_concurrency(urls, destination):
    concurrent = DownloadFilesConcurrently(urls, destination)
    concurrent.download()


def stop_download_multifiles_concurrently():
    from concurrent.futures.thread import ThreadPoolExecutor
    pool = ThreadPoolExecutor()
    pool.shutdown(wait=True)


def download_file_from_mediafire(url, destiation, name):
    mediafire_downloader = MediaFireDownload(url, destiation, name)
    mediafire_downloader.download()


def download_multiple_files_from_mediafire(links, destination, method):
    multiple_mediafire_downloader = MultiMediaFireDownload(links, destination)

    if method == "Multi-Threading":
        multiple_mediafire_downloader.download_parallelly()
    elif method == "Multi-Processing":
        multiple_mediafire_downloader.download_concurrently()
