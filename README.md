
# EasyBar

EasyBar is a flexible Python library for creating and managing progress bars in console applications. It provides an intuitive and customizable way to visualize the progress of operations, enhancing the user experience in command-line interfaces.

## Installation

To install EasyBar, you can use pip:
```bash
pip install easybar
```

## Features

- **Multiple Bars**: Support for managing multiple nested progress bars simultaneously.
- **Color Customization**: Customize the color of the progress bars for better visual distinction.
- **Flexible Configuration**: Set up progress bars with optional prefixes, display styles, margins, and more.
- **Thread Safety**: Ensures safe access in a multi-threaded environment.
- **High Compatibility**: Suitable for multi-OS include Windows, MacOS and Linux



## Usage

### Basic Example

Here's a simple example of how to use `EasyBar` to create a single progress bar:
```python
from easybar.api import EasyBar
import time

def main():
    bar = EasyBar(100, colour='green')
    for _ in bar:
        time.sleep(0.01)  # Simulate some work

if __name__ == "__main__":
    main()
```
This will create a green progress bar that completes over approximately one second.

### Nested Progress Bars

You can manage multiple progress bars at once using `NestedBar`:
```python
from easybar.api import NestedBar
import time

def main():
    nb = NestedBar(100, 3, colour='blue')
    for i in range(101):
        nb.update(0, i)  # Update progress for the first bar
        nb.update(1, i*2)  # Update the second bar at twice the speed
        nb.update(2, i*3)  # Update the third bar at three times the speed
        nb.print_bars()  # Print all bars
        time.sleep(0.1)

if __name__ == "__main__":
    main()
```
This script demonstrates handling three progress bars with different update rates.

## Configuration Options

When initializing `EasyBar` or `NestedBar`, several options can be configured:

- `total` (Numeric): Total value of the progress bar.
- `mode` (str): Mode of the progress bar; defaults to 'default'.
- `prefix` (Optional[str]): Optional prefix text for the progress bar.
- `display` (str): Character used to display the progress; defaults to '█'.
- `fill` (str): Character used to represent incomplete progress; defaults to ' ' (space).
- `margin` (int): Margin size around the progress text.
- `boundary` (str): Characters used to enclose the progress bar; defaults to '[]'.
- `colour` (str): Foreground color of the progress bar.
- `bg_colour` (str): Background color of the progress bar.

## Customizing Colors

EasyBar uses ANSI color codes to customize the appearance of progress bars. Here are the common colors you can use:
- Red
- Green
- Blue
- Yellow
- Cyan
- Magenta
- White

For more information on configuring these options, consult the API documentation provided with the library or check the source code for detailed annotations.

## Conclusion

EasyBar provides a powerful yet simple way to add progress monitoring to your console applications. Whether running lengthy data processing tasks or simple iterative operations, EasyBar offers the tools to visually track progress, making console output more informative and visually appealing.

For further assistance or to report issues, visit the GitHub repository or contact us.