from multiprocessing import Pool
import urllib.request

from service.DownloadProgressBar import DownloadProgressBar


class DownloadFilesConcurently(object):
    def __init__(self, urls, destination):
        self._urls = urls
        self._destination = destination
        self._number_of_processes = len(urls)

    def _get_file(self, link):
        filename = link.split('/')[-1]

        print('Downloading file --> "{filename}"'.format(filename=filename))

        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=filename) as t:
            urllib.request.urlretrieve(link, filename='{}/{}'.format(self._destination, filename),
                                       reporthook=t.update_to)

    def download(self):
        pool = Pool(self._number_of_processes)
        pool.map(self._get_file, self._urls)

        pool.close()
        pool.join()

        print('\nSuccessfully downloaded files from given source!\n')
