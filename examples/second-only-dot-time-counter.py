from picounicorn import PicoUnicorn
import time

# Initialize Pico Unicorn
picounicorn = PicoUnicorn()

# Get width and height
w = picounicorn.get_width()
h = picounicorn.get_height()


# Function to clear the display
def clear_display():
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, 0, 0, 0)


# Function to display the current seconds
def display_seconds(seconds):
    # Clear the previous display
    clear_display()

    # Calculate the number of LEDs to light up
    num_leds = seconds

    # Display the seconds using LEDs
    for i in range(num_leds):
        x = i % w
        y = i // w
        if y < h:  # Ensure we do not go out of bounds
            picounicorn.set_pixel(x, y, 255, 255, 255)  # White color


while True:
    # Get the current time in seconds
    current_time = time.localtime(time.time())
    seconds = current_time[5]  # Extract the seconds from the struct_time tuple

    # Display the current seconds
    display_seconds(seconds)

    # Wait for a second before updating
    time.sleep(1)
