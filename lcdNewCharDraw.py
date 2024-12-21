import tkinter as tk
from tkinter import filedialog, messagebox

# Adjustable scaling factor (MUST BE WHOLE NUMBER RIGHT NOW)
scale_factor = 2

# Variables to track the drag state and fill color
dragging = False
fill_color = "black"

# Function to start drag
def start_drag(event):
    global dragging, fill_color
    dragging = True
    x, y = event.x, event.y
    col, row = x // (20 * scale_factor), y // (20 * scale_factor)
    current_color = canvas.itemcget(grid[row][col], "fill")
    fill_color = "white" if event.num == 3 or current_color == "black" else "black"  # Right-click or toggle

    toggle_pixel(event)

# Function to stop drag
def stop_drag(event):
    global dragging
    dragging = False

# Function to toggle pixel state
def toggle_pixel(event):
    x, y = event.x, event.y
    col, row = x // (20 * scale_factor), y // (20 * scale_factor)
    # Add boundary checks (was paintng when going off grid left or up...)
    if 0 <= col < 5 and 0 <= row < 8:
        canvas.itemconfig(grid[row][col], fill=fill_color)

# Function to drag and paint
def drag(event):
    if dragging:
        toggle_pixel(event)

# Function to clear the grid
def clear_grid():
    for row in grid:
        for cell in row:
            canvas.itemconfig(cell, fill="white")

# Function to show help message
def show_help():
    messagebox.showinfo("Help", "Left click to toggle pixel.\nClick and drag to paint whatever you are toggling current pixel to.\nRight click always erases.\nExport with Save when ready to add character to your project!")

# Function to save grid to a file
def save_grid():
    filename = filename_entry.get().strip()
    if not filename:
        messagebox.showwarning("Warning", "Please enter a filename.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=filename, filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(f"byte {filename}[8] = {{\n")
            for row in grid:
                row_data = "  B"
                for cell in row:
                    color = canvas.itemcget(cell, "fill")
                    row_data += "1" if color == "black" else "0"
                file.write(row_data + ",\n")
            file.write("};\n")
        messagebox.showinfo("Success", f"File saved as {file_path}.")

# Initialize main window
root = tk.Tk()
root.title("5x8 Pixel Painter")

# Create canvas for drawing
canvas_width = 100 * scale_factor
canvas_height = 160 * scale_factor
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Create 5x8 grid of squares
grid = []
for row in range(8):
    grid_row = []
    for col in range(5):
        x1, y1 = col * 20 * scale_factor, row * 20 * scale_factor
        x2, y2 = x1 + 20 * scale_factor, y1 + 20 * scale_factor
        cell = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
        canvas.tag_bind(cell, "<Button-1>", start_drag)
        canvas.tag_bind(cell, "<Button-3>", start_drag)
        canvas.tag_bind(cell, "<B1-Motion>", drag)
        canvas.tag_bind(cell, "<B3-Motion>", drag)
        canvas.tag_bind(cell, "<ButtonRelease-1>", stop_drag)
        canvas.tag_bind(cell, "<ButtonRelease-3>", stop_drag)
        grid_row.append(cell)
    grid.append(grid_row)

# Create filename entry
filename_frame = tk.Frame(root)
filename_frame.pack(pady=5)

filename_label = tk.Label(filename_frame, text="Filename:")
filename_label.pack(side=tk.LEFT)

filename_entry = tk.Entry(filename_frame)
filename_entry.pack(side=tk.LEFT)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack()

save_button = tk.Button(button_frame, text="Save", command=save_grid, bg="#CCFFCC")
save_button.pack(side=tk.LEFT, padx=5)

help_button = tk.Button(button_frame, text="Help", command=show_help, bg="#FFCC80")
help_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_grid, bg="#FFCCCC")
clear_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
