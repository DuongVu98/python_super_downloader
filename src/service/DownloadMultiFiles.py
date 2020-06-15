import urllib.request

from service.ProgressBar import ProgressBar
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


class DownloadFilesParallelly(object):

    def __init__(self, urls, destination):
        self._urls = urls
        self._destination = destination
        self._number_of_processes = len(urls)
        self._pool = ThreadPoolExecutor()

    def _get_file(self, link):
        filename = link.split('/')[-1]

        print('Downloading file --> "{filename}"'.format(filename=filename))

        with ProgressBar(unit='B', unit_scale=True, miniters=1, desc=filename) as t:
            urllib.request.urlretrieve(link, filename='{}/{}'.format(self._destination, filename),
                                       reporthook=t.update_to)

    def download(self):
        self._pool.map(self._get_file, self._urls)


class DownloadFilesConcurrently(object):

    def __init__(self, urls, destination):
        self._urls = urls
        self._destination = destination
        self._number_of_processes = len(urls)

    def _get_file(self, link):
        filename = link.split('/')[-1]

        print('Downloading file --> "{filename}"'.format(filename=filename))

        with ProgressBar(unit='B', unit_scale=True, miniters=1, desc=filename) as t:
            urllib.request.urlretrieve(link, filename='{}/{}'.format(self._destination, filename),
                                       reporthook=t.update_to)

    def download(self):
        try:
            with ProcessPoolExecutor() as executor:
                executor.map(self._get_file, self._urls)
        except KeyboardInterrupt:
            raise
