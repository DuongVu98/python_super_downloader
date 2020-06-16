import urllib.request
import requests
from numpy import arange
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm


class MultiParts:
    def __init__(self, url, file_name, destination, number_of_parts=5):
        self._url = url
        self._number_of_parts = number_of_parts
        self._data_list = []
        self._file_name = file_name
        self._destination = destination

        meta = urllib.request.urlopen(url).info()
        self._file_size = meta.get("Content-Length")

    def _get_single_part(self, range_interval):
        # req = urllib.request.Request(self._url, headers={'Range': range_interval})
        r = requests.get(self._url, stream=True, headers={'Range': range_interval})
        block_size = 1024
        t = tqdm(total=self._file_size, unit='iB', unit_scale=True)
        for data in r.iter_content(block_size):
            t.update(len(data))
            self._data_list.append(data)
        t.close()

    def download(self):
        if not self._file_name:
            print("Size cannot be determined.")
            return
        splits = arange(self._number_of_parts + 1) * (float(self._file_size) / self._number_of_parts)
        range_intervals = []
        for idx in range(self._number_of_parts):
            range_intervals.append("bytes={}-{}".format(splits[idx], splits[idx + 1]))

        with ProcessPoolExecutor() as executor:
            executor.map(self._get_single_part, range_intervals)

        self._get_file_data()
        # for idx in range(self._number_of_parts):
        #     req = urllib.request.Request(self._url, headers={'Range': 'bytes=%d-%d' % (splits[idx], splits[idx + 1])})
        #     self._data_list.append(urllib.request.urlopen(req).read())

    def _get_file_data(self):
        full_data = b''.join(self._data_list)
        with open("{}/{}".format(self._destination, self._file_name)) as f:
            f.write(full_data)
