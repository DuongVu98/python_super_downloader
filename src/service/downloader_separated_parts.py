import threading
import urllib
from numpy import arange


class ThreadedFetch(threading.Thread):
    def __init__(self, url, fileName, splitBy=5):
        super(ThreadedFetch, self).__init__()
        self.__url = url
        self.__spl = splitBy
        self.__dataLst = []
        self.__fileName = fileName
        meta = urllib.request.urlopen(url).info()
        self.__file_size = meta.get("Content-Length")

    def run(self):
        if not self.__file_size:
            print("Size cannot be determined.")
            return
        splits = arange(self.__spl + 1) * (float(self.__file_size) / self.__spl)
        for idx in range(self.__spl):
            req = urllib.request.Request(self.__url, headers={'Range': 'bytes=%d-%d' % (splits[idx], splits[idx + 1])})
            self.__dataLst.append(urllib.request.urlopen(req).read())

    def get_file_data(self):
        return b''.join(self.__dataLst)
