import tkinter as tk
from PIL import Image, ImageTk


def overlay_image(image_path):
    """Overlays the image at the specified path on top of all windows."""
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.01)  # Make the window almost transparent

    # Load the image
    image = Image.open(image_path)
    image_width, image_height = image.size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Center the image on the screen
    image_x = (screen_width - image_width) // 2
    image_y = (screen_height - image_height) // 2

    # Create a label to display the image
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo, bg='black')
    label.place(x=image_x, y=image_y)

    # Remove the window border and make it transparent
    root.overrideredirect(True)
    root.attributes('-alpha', 0.8)  # Adjust the alpha for the image visibility

    root.mainloop()


# Example usage:
overlay_image("crosshair.png")