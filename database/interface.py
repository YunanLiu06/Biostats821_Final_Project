import tkinter as tk
from tryout import Flu_info

root = tk.Tk()

textbox1 = tk.Entry(root)
textbox2 = tk.Entry(root)

button = tk.Button(root, text="Get Information", command=lambda: display_text())

displaybox = tk.Text(root)

textbox1.pack()
textbox2.pack()
button.pack()
displaybox.pack()

def display_text():
    lab_info = Flu_info("Flu_Vaccines_Provider_NC.db")
    text1 = textbox1.get()
    text2 = textbox2.get()
    ll = lab_info.getLimitedLocationByVaccineName(text1, text2)
    displaybox.insert(ll)
    # displaybox.insert(tk.END, f"Text Box 2: {text2}\n")

root.mainloop()
