from tqdm import tqdm
from colorama import Fore

colors = Fore.__dict__


class ProgressBar(tqdm):

    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)
