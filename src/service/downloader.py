from tqdm.auto import tqdm
import urllib
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

