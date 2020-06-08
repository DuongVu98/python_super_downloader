from multiprocessing import Pool
import urllib.request

from service.DownloadProgressBar import DownloadProgressBar

POOL = 8


class DownloadFiles(object):
    def __init__(self, urls, destination):
        self._urls = urls
        self._destination = destination

    def get_file(self, link):
        filename = link.split('/')[-1]

        print('Downloading file --> "{filename}"'.format(filename=filename))

        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=filename) as t:
            urllib.request.urlretrieve(link, filename='{}/{}'.format(self._destination, filename),
                                       reporthook=t.update_to)

    def download(self):
        pool = Pool(POOL)
        pool.map(self.get_file, self._urls)

        pool.close()
        pool.join()

        print('\nSuccessfully downloaded files from given source!\n')
