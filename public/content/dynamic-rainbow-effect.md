---
title: Dynamic Rainbow Effect
date: 2023-07-05
---

# Dynamic Rainbow Effect for Pico Unicorn: Code Explanation

## Overview

This document explains the implementation of a dynamic, shifting rainbow effect for the Pimoroni Pico Unicorn, which features a 16x7 RGB LED matrix. The code creates a smooth, automatically shifting rainbow pattern that can be interactively controlled using the Pico Unicorn's buttons.

## Key Features

1. Automatically shifting rainbow effect
2. Interactive brightness control
3. Interactive saturation control
4. Consistent animation speed

## Code Structure and Implementation

### Libraries and Initialization

```python
from picounicorn import PicoUnicorn
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK
import time

picounicorn = PicoUnicorn()
graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK)
```

We use the `picounicorn` library for hardware control and `picographics` for advanced color manipulation. The `time` module is used for animation timing.

### Global Variables

```python
width = picounicorn.get_width()
height = picounicorn.get_height()
brightness = 1.0
saturation = 1.0
step = 0.05
shift_speed = 0.5
offset = 0
```

These variables control the display dimensions, current brightness and saturation levels, adjustment step size, rainbow shift speed, and the current color offset.

### Display Update Function

```python
def update_display():
    global offset
    for x in range(width):
        hue = (x / width + offset) % 1.0
        pen = graphics.create_pen_hsv(hue, saturation, brightness)
        graphics.set_pen(pen)
        for y in range(height):
            graphics.pixel(x, y)
    picounicorn.update(graphics)
    offset = (offset + shift_speed / width) % 1.0
```

This function is responsible for drawing the rainbow effect:

- It calculates the hue for each column based on its position and the current offset.
- It creates a color pen using HSV (Hue, Saturation, Value) color model, which allows easy manipulation of brightness and saturation.
- It draws a vertical line for each x-coordinate.
- Finally, it updates the display and increments the offset for the next frame.

### Main Loop

```python
while True:
    current_time = time.ticks_ms()
    delta_time = (current_time - last_time) / 1000.0

    # Button controls
    if picounicorn.is_pressed(PicoUnicorn.BUTTON_A):
        brightness = min(1.0, brightness + step)
    # ... (similar for other buttons)

    update_display()

    # Frame rate control
    elapsed = (time.ticks_ms() - current_time) / 1000.0
    if elapsed < 1/30:
        time.sleep(1/30 - elapsed)

    last_time = current_time
```

The main loop handles:

1. Button input for brightness and saturation control
2. Updating the display
3. Maintaining a consistent frame rate

## Design Decisions and Rationale

1. **Use of HSV Color Model**: HSV allows easy separation of hue (color) from saturation and brightness, making it simple to implement the shifting rainbow and controls.

2. **PicoGraphics Library**: This library provides the `create_pen_hsv` function, which simplifies color creation and manipulation.

3. **Global Offset**: The `offset` variable allows the rainbow to shift smoothly over time, creating the dynamic effect.

4. **Button Controls**: Direct manipulation of brightness and saturation provides immediate feedback to the user.

5. **Frame Rate Control**: Aiming for 30 FPS ensures smooth animation while allowing responsive button control.

6. **Step Size**: A small step size (0.05) allows for fine-grained control over brightness and saturation.

## Conclusion

This implementation creates an engaging, interactive display on the Pico Unicorn. It demonstrates effective use of the hardware's capabilities and provides a smooth, customizable visual effect. The code structure allows for easy modifications and extensions, such as adding new effects or control schemes.
