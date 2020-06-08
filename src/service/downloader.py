from tqdm.auto import tqdm
import urllib

from service.downloader_separated_parts import ThreadedFetch


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
