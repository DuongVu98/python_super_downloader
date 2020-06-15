from multiprocessing import Pool
import urllib.request

from service.ProgressBar import ProgressBar
from concurrent.futures import ThreadPoolExecutor


class DownloadFilesConcurently(object):
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
        # pool = Pool(self._number_of_processes, initargs=(ProgressBar.get_lock(),))
        # pool.map(self._get_file, self._urls)
        #
        # pool.close()
        # pool.join()

        # pool = ThreadPoolExecutor()
        self._pool.map(self._get_file, self._urls)

        print('\nSuccessfully downloaded files from given source!\n')

    def stop(self):
        self._pool.shutdown(wait=True)
