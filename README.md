# Pure Python Image Processor

## Overview

This project is a small grayscale image processor that applies pixel-wise, geometric and neighborhood operations to an image. It uses pure Python only: no NumPy, OpenCV or Pillow. Every operation is written by hand with loops and lists.

## Requirements

- Python <your version, e.g. 3.10.12> (check with `python3 --version`)
- No external libraries (standard library only)

## How to Run

```bash
git clone https://github.com/kotharideev08-sys/pure-python-image-processor.git
cd pure-python-image-processor
python3 main.py
```

## Image Representation

A grayscale image is a list of lists of integers. `image[r][c]` is the pixel at row `r`, column `c`, and each value is between 0 (black) and 255 (white).

```python
image = [
    [  0, 128, 255],
    [ 64, 192,  32],
]
# image[1][2] == 32   (row 1, column 2)
```

The height is `len(image)` and the width is `len(image[0])`.

## Operations

**Pixel-wise** (each output pixel depends only on the same input pixel)
- `invert(image)`: replaces each value `v` with `255 - v`.
- `threshold(image, t)`: sets pixels to 255 if `v >= t`, otherwise 0.
- `adjust_brightness(image, amount)`: adds `amount` to every pixel, clamped to 0-255.

**Geometric** (pixels move to new positions)
- `flip_horizontal(image)`: mirrors the image left to right.
- `flip_vertical(image)`: mirrors the image top to bottom.
- `rotate_90(image)`: rotates the image 90 degrees clockwise.

**Neighborhood** (each output pixel depends on nearby pixels)
- `box_blur_valid(image)`: 3x3 box blur that averages only the neighbors that exist inside the image.

## Border Handling

**Strategy chosen:** `box_blur_valid` averages only the valid neighbors. For each pixel it looks at the 3x3 window around it, skips any positions that fall outside the image, and averages the rest.

**Why:** the edges get blurred like the rest of the image, and they don't darken. Padding with zeros would pull edge pixels toward black, because the missing neighbors would count as 0.

**Downside:** edge and corner pixels are averaged over fewer neighbors (6 on an edge, 4 in a corner, instead of 9 in the interior). They are a bit noisier, because each neighbor has more weight in the average.

**How the original is protected:** all reads come from the input image, and all writes go to a separate result image. This means blurred values never feed back into later calculations, and the input is never modified.

## Sample Output
## Sample Output

All operations take a 5x5 grayscale image (values 0-255) and return a new image. The original is never modified.

### Original
```text
255  10 220  50 110
 23 255   0  20 200
  0   0 255   0   0
  0  45   0 255   0
100   0 195   0 255
```

### Inverted
```text
  0 245  35 205 145
232   0 255 235  55
255 255   0 255 255
255 210 255   0 255
155 255  60 255   0
```

### Brighter (+120)
```text
255 130 255 170 230
143 255 120 140 255
120 120 255 120 120
120 165 120 255 120
220 120 255 120 255
```

### Darker (-120)
```text
135   0 100   0   0
  0 135   0   0  80
  0   0 135   0   0
  0   0   0 135   0
  0   0  75   0 135
```

### Threshold
```text
255   0 255   0 255
  0 255   0   0 255
  0   0 255   0   0
  0   0   0 255   0
255   0 255   0 255
```

### Flip Vertical
```text
100   0 195   0 255
  0  45   0 255   0
  0   0 255   0   0
 23 255   0  20 200
255  10 220  50 110
```

### Flip Horizontal
```text
110  50 220  10 255
200  20   0 255  23
  0   0 255   0   0
  0 255   0  45   0
255   0 195   0 100
```

### Rotate 90° Clockwise
```text
100   0   0  23 255
  0  45   0 255  10
195   0 255   0 220
  0 255   0  20  50
255   0   0 200 110
```

### Rotate 90° Anticlockwise
```text
110 200   0   0 255
 50  20   0 255   0
220   0 255   0 195
 10 255   0  45   0
255  23   0   0 100
```

### Crop (2x2, top=2, left=2)
```text
255   0
  0 255
```

### Box Blur (3x3, average of valid neighbors at borders)
```text
136 127  92 100  95
 90 113  90  95  63
 54  64  92  81  79
 24  66  83 107  85
 36  57  82 118 128
```

### Original Again (unchanged)
```text
255  10 220  50 110
 23 255   0  20 200
  0   0 255   0   0
  0  45   0 255   0
100   0 195   0 255
```

## Aliasing and Copying

Every function builds a new image and returns it, so the input image is never changed. Lists are shared by reference in Python, so reusing the input's rows would silently change the original too.

This is also why `[[0] * 3] * 3` is a bug. It creates three references to the same row, so changing one row changes all three. The list comprehension `[[0] * 3 for _ in range(3)]` builds a fresh row each time, so the rows are independent. The functions here use the second form to create their result images.

## Limitations

- Grayscale only (no RGB support).
- The blur uses a fixed 3x3 kernel.
- Results are rounded to integers, so repeated operations can accumulate small rounding errors.
