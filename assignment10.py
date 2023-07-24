import tkinter as tk
import webbrowser

def navigate_to_site():
    url = entry.get()
    print(f"Navigating to '{url}'")
    webbrowser.open(url)

root = tk.Tk()
root.title("Web ")

label = tk.Label(root, text="Enter a website URL:")
label.pack(pady=10)

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

go_button = tk.Button(root, text="Go", command=navigate_to_site)
go_button.pack(pady=20)


root.mainloop()
