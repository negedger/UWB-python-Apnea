import tkinter as tk
import math

# Create the main window
window = tk.Tk()
window.title("Animated Flower Pattern")

# Create a canvas to draw on
canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Define the flower pattern parameters
center_x = canvas_width // 2
center_y = canvas_height // 2
petal_radius = [80]
num_petals = 12
rotation_angle = 30
animation_speed = 5

# Draw the flower pattern
petal_color = "#00ff00"
for _ in range(num_petals):
    canvas.create_oval(
        center_x - petal_radius[0],
        center_y - petal_radius[0],
        center_x + petal_radius[0],
        center_y + petal_radius[0],
        fill=petal_color,
    )
    petal_radius[0] -= 5


# Animation function
def animate(petal_radius):
    # Clear the canvas
    canvas.delete("all")

    # Draw the flower pattern
    for angle in range(0, 360, rotation_angle):
        # Rotate the petal's coordinates
        rotated_coords = rotate(angle, (center_x, center_y - petal_radius[0]))

        # Calculate the new petal's position
        petal_x = rotated_coords[0]
        petal_y = rotated_coords[1]

        # Draw the petal
        canvas.create_oval(
            petal_x - petal_radius[0],
            petal_y - petal_radius[0],
            petal_x + petal_radius[0],
            petal_y + petal_radius[0],
            fill=petal_color,
        )

        # Decrease the petal radius for animation effect
        petal_radius[0] -= 0.1

    # Increase the petal radius for the next frame
    petal_radius[0] += 0.1

    # Schedule the next animation frame
    window.after(animation_speed, animate, petal_radius)


# Helper function to rotate coordinates
def rotate(angle, coords):
    radian = angle * (3.14159 / 180)
    cos_val = math.cos(radian)
    sin_val = math.sin(radian)
    x = coords[0] * cos_val - coords[1] * sin_val
    y = coords[0] * sin_val + coords[1] * cos_val
    return (x, y)


# Start the animation
animate(petal_radius)

# Run the main event loop
window.mainloop()
