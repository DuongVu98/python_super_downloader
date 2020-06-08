import urllib.request

from service.DownloadProgressBar import DownloadProgressBar
from service.ThreadedFetch import ThreadedFetch
from service.DownloadFiles import DownloadFiles


def download_default(url, destination, file_name):
    if file_name is None:
        file_name = url.split('/')[-1]

    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=file_name) as t:
        urllib.request.urlretrieve(url, filename="{}/{}".format(destination, file_name), reporthook=t.update_to)


def download_separated_threads(url, destination, file_name):
    if file_name is None:
        file_name = url.split('/')[-1]

    dl = ThreadedFetch(url, file_name)
    dl.start()
    dl.join()
    content = dl.get_file_data()
    if content:
        with open("{}/{}".format(destination, file_name), 'w') as fh:
            fh.write(str(content))
        print("Finished Writing file %s" % file_name)


def download_multithreading(urls, destination):
    d = DownloadFiles(urls, destination)
    d.download()
