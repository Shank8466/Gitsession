import tkinter as tk
import webbrowser

def navigate_to_site():
    url = entry.get()
    print(f"Navigating to '{url}'")
    webbrowser.open(url)

# Create the main application window
root = tk.Tk()
root.title("Web Navigator")

# Label to display instructions
label = tk.Label(root, text="Enter a website URL:")
label.pack(pady=10)

# Entry widget to get user input
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Button to trigger navigation
go_button = tk.Button(root, text="Go", command=navigate_to_site)
go_button.pack(pady=10)

# Run the application
root.mainloop()
