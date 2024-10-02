import tkinter as tk
from gpiozero import LED

# Setup GPIO pins for the LEDs
# Assign LED objects to GPIO pins (17 for red, 27 for green, 22 for yellow)
red_led = LED(17)
green_led = LED(27)
yellow_led = LED(22) 

# Turn off all LEDs initially to ensure they start in an off state
red_led.off()
green_led.off()
yellow_led.off()

# Function to turn on the selected LED and turn off the others
def select_led():
    selected_led = led_choice.get()  # Get the currently selected LED option
    if selected_led == 'red':
        red_led.on()      # Turn on the red LED
        green_led.off()   # Turn off the green LED
        yellow_led.off()  # Turn off the yellow LED
    elif selected_led == 'green':
        red_led.off()     # Turn off the red LED
        green_led.on()    # Turn on the green LED
        yellow_led.off()  # Turn off the yellow LED
    elif selected_led == 'yellow':
        red_led.off()     # Turn off the red LED
        green_led.off()   # Turn off the green LED
        yellow_led.on()   # Turn on the yellow LED

# Function to exit the GUI and turn off all LEDs before quitting
def exit_gui():
    red_led.off()        # Turn off the red LED
    green_led.off()      # Turn off the green LED
    yellow_led.off()     # Turn off the yellow LED
    root.destroy()       # Close the Tkinter window

# Create the main window for the GUI
root = tk.Tk()
root.title("LED Controller")  # Set the title of the window

# Variable to store the selected LED option ('red', 'green', or 'yellow')
led_choice = tk.StringVar(value="red")  # Default selection is "red"

# Create radio buttons for the user to select which LED to turn on
tk.Radiobutton(root, text="Red", variable=led_choice, value="red", command=select_led).pack(anchor=tk.W)
tk.Radiobutton(root, text="Green", variable=led_choice, value="green", command=select_led).pack(anchor=tk.W)
tk.Radiobutton(root, text="Yellow", variable=led_choice, value="yellow", command=select_led).pack(anchor=tk.W)

# Create an Exit button to allow the user to quit the application
exit_button = tk.Button(root, text="Exit", command=exit_gui)
exit_button.pack()  # Display the button

# Start the Tkinter main loop to run the GUI
root.mainloop()