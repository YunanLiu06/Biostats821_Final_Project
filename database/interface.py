import tkinter as tk
from tryout import Flu_info

root = tk.Tk()

tk.Label(root, text="Vaccine Name: ").grid(row=0)
tk.Label(root, text="Optional Filters: ").grid(row=1, columnspan=2)
tk.Label(root, text="Number of locations needed: ").grid(row=2)
tk.Label(root, text="Latitude of your location: ").grid(row=3)
tk.Label(root, text="Longitude of your location: ").grid(row=4)

options = [
    "Flu Shot",
    "Flu Shot (Egg free)",
    "Flu Shot (65+, high-dose or adjuvanted)",
    "Flu Nasal Spray"
]
clicked = tk.StringVar()
clicked.set("Choose Vaccine")
drop = tk.OptionMenu( root , clicked , *options )

# textbox1 = tk.Entry(root)
textbox2 = tk.Entry(root)
textbox3 = tk.Entry(root)
textbox4 = tk.Entry(root)
drop.grid(row=0, column=1)
textbox2.grid(row=2, column=1)
textbox3.grid(row=3, column=1)
textbox4.grid(row=4, column=1)

button = tk.Button(
    root, text="Get Information", command=lambda: display_text()
)
clean_button = tk.Button(
    root, text="Clear Text Box", command=lambda: clean_up()
)

displaybox = tk.Text(root)

button.grid(row=5, columnspan=2)
clean_button.grid(row=6, columnspan=2)
displaybox.grid(row=7, columnspan=2)


def display_text():
    # lab_info = Flu_info("Flu_Vaccines_Provider_NC.db")
    text1 = clicked.get()
    text2 = textbox2.get()
    text3 = textbox3.get()
    text4 = textbox4.get()
    if text1 == "Choose Vaccine":
        ll = "Please select the vaccine you want to check."
    elif len(text2) == 0:
        # ll = lab_info.getLocationByVaccineName(text1)
        ll = "1"
    elif len(text3) != 0 and len(text4) != 0:
        # ll = lab_info.getInfoByPosition(text3, text4)
        ll = "2"
    elif len(text3) != 0 or len(text4) != 0:
        ll = "Please enter the full location info!"
    else:
        # ll = lab_info.getLimitedLocationByVaccineName(text1, int(text2))
        ll = "3"
    displaybox.insert(tk.END, ll)


def clean_up():
    clicked.set("Choose Vaccine")
    textbox2.delete(0, tk.END)
    textbox3.delete(0, tk.END)
    textbox4.delete(0, tk.END)
    displaybox.delete("1.0", tk.END)


root.mainloop()
