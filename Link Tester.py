import tkinter as tk
from tkinter import messagebox
import requests

def test_link():
    link = entry.get()

    try:
        response = requests.get(link)

        if response.status_code == 200:
            messagebox.showinfo("Link Test", "Link is working fine!")
        elif response.status_code == 404:
            messagebox.showerror("Link Test", "Link is broken. Error 404: Page not found.")
        else:
            messagebox.showerror("Link Test", "Link is not working. Status code: {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Link Test", "An error occurred: {}".format(str(e)))

# Create the main window
window = tk.Tk()
window.title("Link Tester")

# Create the label and entry widget for entering the link
label = tk.Label(window, text="Enter a link:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Create the button for testing the link
button = tk.Button(window, text="Test Link", command=test_link)
button.pack()

# Run the main event loop
window.mainloop()
