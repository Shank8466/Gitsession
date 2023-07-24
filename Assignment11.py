import tkinter as tk
import webbrowser

def navigate_to_faq():
    name = name_entry.get()
    source = source_var.get()

    # Dictionary to map sources to their respective FAQ URLs
    sources_to_faq = {
        "YouTube Ads": "https://www.example.com/faq/youtube",
    }

    if source in sources_to_faq:
        faq_url = sources_to_faq[source]
        print(f"Hello {name}, navigating to the FAQ page for {source}...")
        webbrowser.open(faq_url)
    else:
        print("Invalid source selection!")

root = tk.Tk()
root.title("Course Enquiry Form")

name_label = tk.Label(root, text="Your Name:")
name_label.pack(pady=5)

name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

source_label = tk.Label(root, text="Where did you hear about us?")
source_label.pack(pady=5)

sources = [ "YouTube Ads"]
source_var = tk.StringVar(root)
source_var.set(sources[0])  
source_dropdown = tk.OptionMenu(root, source_var, *sources)
source_dropdown.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=navigate_to_faq)
submit_button.pack(pady=10)

root.mainloop()
