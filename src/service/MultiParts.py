import urllib.request
import requests
from numpy import arange
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm


class MultiParts:
    def __init__(self, url, file_name, destination, number_of_parts=5):
        self._url = url
        self._number_of_parts = number_of_parts
        self._data_list = dict()
        self._file_name = file_name
        self._destination = destination

        meta = urllib.request.urlopen(url).info()
        self._file_size = int(meta.get("Content-Length"))
        print(meta.get("Content-Length"))
        print(self._file_size)

    def _get_single_part(self, idx, range_interval):
        r = requests.get(self._url, stream=True, headers={'Range': range_interval})
        block_size = 1024
        t = tqdm(total=self._file_size, unit='iB', unit_scale=True)
        full_part = b""
        for data in r.iter_content(block_size):
            t.update(len(data))
            full_part += data
        t.close()
        # self._data_list.append(full_part)
        # print(full_part)
        self._data_list[idx] = str(full_part)

    def download(self):
        if not self._file_name:
            print("Size cannot be determined.")
            return
        splits = arange(self._number_of_parts + 1) * (self._file_size / self._number_of_parts)
        range_intervals = []
        idx_ranges = []
        for idx in range(self._number_of_parts):
            idx_ranges.append(idx)
            range_intervals.append("bytes={}-{}".format(splits[idx], splits[idx + 1]))
        print(range_intervals)
        with ProcessPoolExecutor() as executor:
            executor.map(self._get_single_part, idx_ranges, range_intervals)

        self._get_file_data()

    def _get_file_data(self):
        print(len(self._data_list))
        # full_data = ''.join(self._data_list)
        # with open("{}/{}".format(self._destination, self._file_name), "w") as f:
        #     f.write(full_data)
