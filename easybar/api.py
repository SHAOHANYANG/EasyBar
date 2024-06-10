import sys

from .utils import Bar, Numeric
from .exceptions import EasyBarException

from typing import Optional, Callable
import time as _time


class EasyBar(Bar):

    def __init__(self, total: Numeric, *args, **kwargs):
        super().__init__(total, *args, **kwargs)

        # Progress to be updated
        self._inc = 1

    def update(self):
        with self._lock:
            self._progress += self._inc
            self.print_bar()

    def print_bar(self):
        progress = self._progress / self._total

        if self._mode == 'fraction':
            progress_str = f'{self._progress} / {self._total}'
        else:
            progress_str = f'{(progress * 100):.2f}%'

        prefix_len = len(self._prefix)
        progress_len = len(progress_str)
        boundary_len = len(self._boundary)
        bar_len = self._window_size - prefix_len - \
            progress_len - boundary_len - self._margin
        display_len = int(bar_len * progress)
        fill_len = bar_len - display_len

        prefix = self._prefix
        display = self._display * display_len
        fill = self._fill * fill_len
        start, end = self._boundary

        bar = '\r' + prefix + start + display + fill + \
            end + progress_str
        coloured_bar = self.colour_txt(bar, self._colour, self._bg_colour)

        print(coloured_bar, end='', flush=True)

    def inc(self, inc):
        self._inc = inc

class NestedBar(Bar):
    def __init__(self, total, num_bars=1, bar_length=50, *args, **kwargs):
        super().__init__(total, *args, **kwargs)
        self.total = total
        self.num_bars = num_bars
        self.current = [0] * num_bars
        self.bar_length = bar_length

    def update(self, bar_id: int, progress: Numeric):
        """Update the progress of a specific bar."""
        progress = min(progress, self.total)
        self.current[bar_id] = progress
        # Optionally print the bar
        # self.print_bar()

    def get_progress(self):
        """Get current progress state."""
        return self.current

    def print_bars(self):
        """Prints all progress bars to the terminal with colors, based on user configuration."""
        sys.stdout.write("\033[{}F".format(self.num_bars + 1))
        sys.stdout.write("\033[2K")

        # Creating the full progress line
        full_progress = int(self.bar_length * sum(self.current) / (self.total * self.num_bars))
        total_line = f"{self._prefix + ': ' if self._prefix else ''}{self._boundary[0]}" + \
                     self._display * full_progress + \
                     self._fill * (self.bar_length - full_progress) + \
                     f"{self._boundary[1]} {int(100 * sum(self.current) / (self.total * self.num_bars))}%\n"
        # Applying color to the total progress line and printing it
        sys.stdout.write(self.colour_txt(total_line, self._colour, self._bg_colour))

        # Loop through each bar and format accordingly
        for bar_id in range(self.num_bars):
            sys.stdout.write("\033[2K")
            bar_line = f"{self._prefix} {bar_id + 1}: {self._boundary[0]}" if self._prefix else f"Bar {bar_id + 1}: {self._boundary[0]}"
            bar_line += self._display * int(self.bar_length * self.current[bar_id] / self.total)
            bar_line += self._fill * (self.bar_length - int(self.bar_length * self.current[bar_id] / self.total))
            bar_line += f"{self._boundary[1]} {int(100 * self.current[bar_id] / self.total)}%\n"
            # Applying color to each bar's progress line and printing it
            sys.stdout.write(self.colour_txt(bar_line, self._colour, self._bg_colour))


        sys.stdout.flush()


def retry(func: Callable, max: Optional[int] = None,
          *args, **kwargs) -> Callable:
    def inner(*args, **kwargs):
        bar = EasyBar(max, *args, **kwargs)

        for _ in bar:
            try:
                res = func(*args, **kwargs)
                break
            except Exception as e:
                msg = f'Failed to execute {func.__name__}: {e}'

            _time.sleep(0)
        else:
            msg = f'Failed to execute {func.__name__} after {max} retries'

            raise EasyBarException(msg)

        return res

    return inner


def loop(func: Callable, times: Optional[int] = None,
         *args, **kwargs) -> Callable:
    _args = args
    _kwargs = kwargs

    def inner(*args, **kwargs):
        if times is not None:
            remaining = times
        else:
            remaining = float("inf")

        for _ in Bar(remaining, _args, _kwargs):
            try:
                yield func(*args, **kwargs)
            except Exception as e:
                msg = f'Failed to execute {func.__name__}: {e}'

                raise EasyBarException(msg)

    return inner



# Demo1
def main():
    barA = EasyBar(100, colour='green')
    barB = EasyBar(100, colour='red')

    for _ in barA:
        _time.sleep(0.01)

    for i in barB:
        with open('tmp.txt', 'at') as f:
            f.write(str(i))


if __name__ == '__main__':
    main()
