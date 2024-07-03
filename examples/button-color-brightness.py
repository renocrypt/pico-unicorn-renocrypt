from picounicorn import PicoUnicorn
import time

# Initialize Pico Unicorn
picounicorn = PicoUnicorn()

# Define colors
colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
]
current_color_index = 0

# Initialize brightness
brightness = 1.0

# Get width and height
w = picounicorn.get_width()
h = picounicorn.get_height()


# Function to apply brightness to a color
def apply_brightness(color, brightness):
    return tuple(int(c * brightness) for c in color)


# Function to fill the screen with a color and brightness
def fill_screen(r, g, b, brightness):
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(
                x, y, int(r * brightness), int(g * brightness), int(b * brightness)
            )


# Set initial color
fill_screen(*colors[current_color_index], brightness)

while True:
    if picounicorn.is_pressed(picounicorn.BUTTON_A):
        # Change to the next color
        current_color_index = (current_color_index + 1) % len(colors)
        fill_screen(*colors[current_color_index], brightness)

        # Debounce delay to prevent multiple presses
        time.sleep(0.3)

    if picounicorn.is_pressed(picounicorn.BUTTON_X):
        # Increase brightness
        brightness = min(1.0, brightness + 0.1)
        fill_screen(*colors[current_color_index], brightness)

        # Debounce delay
        time.sleep(0.3)

    if picounicorn.is_pressed(picounicorn.BUTTON_Y):
        # Decrease brightness
        brightness = max(0.0, brightness - 0.1)
        fill_screen(*colors[current_color_index], brightness)

        # Debounce delay
        time.sleep(0.3)
