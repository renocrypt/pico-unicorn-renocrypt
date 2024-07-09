---
title: PicoUnicorn MicroPython Library Documentation
date: 2023-07-01
---

# PicoUnicorn MicroPython Library Documentation

## Introduction

The PicoUnicorn library is designed for use with the Pimoroni Pico Unicorn Pack, which features a 16x7 matrix of RGB LEDs (112 total) for the Raspberry Pi Pico. This documentation covers the basics of using the library to control the LED matrix and buttons on the Pico Unicorn.

## Installation

Ensure you have the `picounicorn` library installed on your Raspberry Pi Pico. You may also need the `picographics` library for advanced graphics capabilities.

## Basic Usage

### Importing the Library

```python
from picounicorn import PicoUnicorn
```

### Initializing PicoUnicorn

```python
picounicorn = PicoUnicorn()
```

## Display Control

### Getting Display Dimensions

```python
width = picounicorn.get_width()   # Returns 16
height = picounicorn.get_height() # Returns 7
```

### Setting Pixel Colors

Set individual pixel colors using RGB values (0-255):

```python
picounicorn.set_pixel(x, y, r, g, b)
```

### Clearing the Display

To turn off all LEDs:

```python
for x in range(width):
    for y in range(height):
        picounicorn.set_pixel(x, y, 0, 0, 0)
```

## Button Input

The Pico Unicorn has four buttons: A, B, X, and Y.

### Checking Button State

```python
if picounicorn.is_pressed(picounicorn.BUTTON_A):
    # Button A is pressed
```

Available button constants:

- `picounicorn.BUTTON_A`
- `picounicorn.BUTTON_B`
- `picounicorn.BUTTON_X`
- `picounicorn.BUTTON_Y`

## Advanced Graphics with PicoGraphics

For more advanced graphics capabilities, you can use the `PicoGraphics` library in conjunction with PicoUnicorn.

### Importing and Initializing PicoGraphics

```python
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK

graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK)
```

### Creating and Using Pens

```python
# Create a pen with RGB values
pen = graphics.create_pen(r, g, b)

# Create a pen with HSV values
hsv_pen = graphics.create_pen_hsv(h, s, v)

# Set the current pen
graphics.set_pen(pen)

# Draw a pixel
graphics.pixel(x, y)
```

### Updating the Display

After drawing with PicoGraphics, update the Pico Unicorn display:

```python
picounicorn.update(graphics)
```

## Example Projects

### Rainbow Effect

Create a scrolling rainbow effect across the LED matrix:

```python
import time
from picounicorn import PicoUnicorn
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK

picounicorn = PicoUnicorn()
graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK)

w = picounicorn.get_width()
h = picounicorn.get_height()

while True:
    t = time.ticks_ms() / 3600
    for x in range(w):
        for y in range(h):
            pen = graphics.create_pen_hsv(t + ((x + y) / w / 4), 1.0, 1.0)
            graphics.set_pen(pen)
            graphics.pixel(x, y)

    picounicorn.update(graphics)
    time.sleep(1.0 / 60)
```

### Fire Effect

Implement a procedural fire effect:

```python
# (Refer to the vertical-fire.py example for the full implementation)
```

## Tips and Best Practices

1. Use `micropython.native` decorator for performance-critical functions.
2. Limit updates to around 60 fps for smooth animations.
3. Take advantage of both `picounicorn` and `picographics` libraries for more versatile graphics capabilities.
4. Remember to call `picounicorn.update(graphics)` after drawing with PicoGraphics.

## Conclusion

The PicoUnicorn library provides an easy-to-use interface for controlling the Pico Unicorn Pack's LED matrix and buttons. Combined with the PicoGraphics library, it offers powerful graphics capabilities for creating eye-catching displays and interactive projects with your Raspberry Pi Pico.
