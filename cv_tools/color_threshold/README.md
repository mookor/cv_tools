# Color Threshold Finder

An interactive tool for finding optimal HSV color thresholds in images using OpenCV trackbars.

## Features

- **Interactive HSV adjustment** with real-time visual feedback
- **Multiple display modes** for original image, mask, and filtered result
- **Save/load functionality** to persist color thresholds
- **Flexible input** - works with both file paths and numpy arrays

## Installation

Requires Python 3.10+ and the following dependencies:

```bash
pip install opencv-python numpy
```

## Quick Start

### Command Line

After installing the package, use the `color-threshold` command:

```bash
# Basic usage (shows result by default)
color-threshold image.png

# Show all windows
color-threshold image.png --all

# Show specific windows
color-threshold image.png --mask --result

# Custom output file
color-threshold image.png --output my_thresholds.txt
```

Or use it as a Python module:

```bash
python -m cv_tools.color_threshold image.png --all
```

### Python API

```python
from cv_tools.color_threshold import ColorThresholdFinder

# Load image and start interactive threshold finder
finder = ColorThresholdFinder(
    image_path='image.png',
    display_image=True,
    display_mask=True,
    display_result=True
)

finder.find_color_threshold()
```

## Usage

### Basic Example

```python
finder = ColorThresholdFinder('path/to/image.png')
finder.find_color_threshold()
```

### With Numpy Array

```python
import cv2

image = cv2.imread('image.png')
finder = ColorThresholdFinder(image=image, display_mask=True)
finder.find_color_threshold()
```

### Custom Thresholds File

```python
finder = ColorThresholdFinder(
    image_path='image.png',
    display_result=True,
    thresholds_path='my_thresholds.txt'
)
finder.find_color_threshold()
```

## Command Line Options

```
usage: color-threshold [-h] [-i] [-m] [-r] [-a] [-o OUTPUT] image

positional arguments:
  image                 Path to the input image

optional arguments:
  -h, --help            Show help message and exit
  -i, --show-image      Display original image window
  -m, --mask            Display binary mask window
  -r, --result          Display filtered result window
  -a, --all             Display all windows (image, mask, and result)
  -o OUTPUT, --output OUTPUT
                        Output file path for saving thresholds (default: thresholds.txt)
```

## Controls

| Key | Action |
|-----|--------|
| **Q** | Quit the application |
| **S** | Save current thresholds to file |

## Trackbars

Adjust these sliders in real-time to find the perfect color range:

- **Hue Min/Max** (0-179) - Color selection
- **Sat Min/Max** (0-255) - Color saturation
- **Val Min/Max** (0-255) - Brightness level

## Parameters

### `__init__` Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `image_path` | `str \| None` | `None` | Path to the image file |
| `image` | `np.ndarray \| None` | `None` | Image as numpy array |
| `display_image` | `bool` | `False` | Show original image window |
| `display_mask` | `bool` | `False` | Show binary mask window |
| `display_result` | `bool` | `True` | Show filtered result window |
| `thresholds_path` | `str` | `"thresholds.txt"` | File path for saving thresholds |

**Note:** Either `image_path` or `image` must be provided.

## Output Format

When saving thresholds (press **S**), the file contains:

```
Lower: [h_min, s_min, v_min]
Upper: [h_max, s_max, v_max]
```


## Use Cases

- **Color detection** - Find objects of specific colors
- **Image segmentation** - Isolate colored regions
- **Computer vision preprocessing** - Fine-tune color filters
- **Object tracking** - Determine optimal color ranges for tracking

## Tips

1. Start with all trackbars at default values
2. Enable `display_mask=True` to see what's being detected
3. Enable `display_result=True` to see the final filtered image
4. Adjust Hue first to select the general color range
5. Fine-tune with Saturation and Value for precision
6. Save your thresholds when satisfied (press **S**)


