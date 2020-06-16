import re
import threading

import requests
import urllib.request

from service.DownloadMultiFiles import DownloadFilesConcurrently, DownloadFilesParallelly
from service.ProgressBar import ProgressBar

media_fire_pattern = '<a\s[^<]*href="(.*)">\s*Download'


def _download_single_thread(url, destination, progress_bar_position):
    file_name = url.split('/')[-1]

    with ProgressBar(unit='B', unit_scale=True, miniters=1, desc=file_name,
                     position=progress_bar_position) as t:
        urllib.request.urlretrieve(url, filename="{}/{}".format(destination, file_name), reporthook=t.update_to)


def get_url_from_mediafire_link(link):
    r = requests.get(link)
    regex_results = re.findall(media_fire_pattern, r.text)
    return regex_results[0]


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

        _download_single_thread(download_url, self._destination, 0)


class MultiMediaFireDownload:
    def __init__(self, mediafire_links, destination):
        self._mediafire_links = mediafire_links
        self._destination = destination
        self._urls = []

    def _get_all_web_sources(self):
        web_sources = []
        for link in self._mediafire_links:
            web_sources.append(requests.get(link).text)

        return web_sources

    def _get_all_download_urls(self):
        web_sources = self._get_all_web_sources()

        for source in web_sources:
            regex_result = re.findall(media_fire_pattern, source)
            self._urls.append(regex_result[0])

    def download_concurrently(self):
        self._get_all_download_urls()

        concurrent = DownloadFilesConcurrently(self._urls, self._destination)
        concurrent.download()

    def download_parallelly(self):
        self._get_all_download_urls()

        parallel = DownloadFilesParallelly(self._urls, self._destination)
        parallel.download()
