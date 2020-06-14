import re
import requests
import urllib.request

from service.ProgressBar import ProgressBar

media_fire_pattern = '<a\s[^<]*href="(.*)">\s*Download'


class MediaFireDownload:
    def __init__(self, mediafire_link, destination, name):
        self._mediafire_link = mediafire_link
        self._destination = destination
        self._file_name = name

    def _get_web_source(self):
        r = requests.get(self._mediafire_link)
        return r.text

    def _get_download_url(self):
        regex_results = re.findall(media_fire_pattern, self._get_web_source())
        return regex_results[0]

    def download(self):
        download_url = self._get_download_url()

        if self._file_name is None:
            self._file_name = download_url.split('/')[-1]

        with ProgressBar(unit='B', unit_scale=True, miniters=1, desc=self._file_name) as t:
            urllib.request.urlretrieve(download_url, filename="{}/{}".format(self._destination, self._file_name), reporthook=t.update_to)
