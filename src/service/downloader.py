from tqdm.auto import tqdm
from numpy import arange
import urllib
import threading
import requests
import progressbar


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_default(url, destination, file_name):
    if file_name is None:
        file_name = url.split('/')[-1]

    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=file_name) as t:
        urllib.request.urlretrieve(url, filename="{}/{}".format(destination, file_name), reporthook=t.update_to)


class ThreadedFetch(threading.Thread):
    def __init__(self, url, fileName, splitBy=5):
        super(ThreadedFetch, self).__init__()
        self.__url = url
        self.__spl = splitBy
        self.__dataLst = []
        self.__fileName = fileName
        self.__file_size = requests.head(self.__url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)

    def run(self):
        if not self.__file_size:
            print("Size cannot be determined.")
            return
        splits = arange(self.__spl + 1) * (float(self.__file_size) / self.__spl)
        for idx in range(self.__spl):
            self.__dataLst.append(
                urllib.request.urlopen(self.__url, headers={'Range': 'bytes=%d-%d' % (splits[idx], splits[idx + 1])}))

    def getFileData(self):
        return ''.join(self.__dataLst)


def download_separated_threads(url, destination, file_name):
    if file_name is None:
        file_name = url.split('/')[-1]

    dl = ThreadedFetch(url, file_name)
    dl.start()
    dl.join()
    content = dl.getFileData()
    if content:
        with open("{}/{}".format(destination, file_name), 'w') as fh:
            fh.write(content)
        print("Finished Writing file %s" % file_name)
