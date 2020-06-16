from time import sleep
from tqdm import tqdm, trange
from concurrent.futures import ThreadPoolExecutor

L = list(range(9))


def progresser(n):
    interval = 0.001 / (n + 2)
    total = 5000
    text = "#{}, est. {:<04.2}s".format(n, interval * total)
    for _ in trange(total, desc=text):
        sleep(interval)
    if n == 6:
        tqdm.write("n == 6 completed.")
        tqdm.write("`tqdm.write()` is thread-safe in py3!")


def draft():
    # from service.DownloadFilesConcurrently import DownloadFilesConcurently
    # urls = [
    #     "http://quatest1.com.vn/images/PHP-DocumentFull.pdf",
    #     "http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf"
    #     "https://riptutorial.com/Download/node-js.pdf"
    # ]
    # destination = "downloaded"
    # d = DownloadFilesConcurently(urls, destination)
    # d.download()
    pass


if __name__ == '__main__':
    with ThreadPoolExecutor() as p:
        p.map(progresser, L)
