"""GUI for the database project."""
import tkinter as tk
from get_info import Flu_info

root = tk.Tk()

tk.Label(root, text="Vaccine Name: ").grid(row=0)
tk.Label(root, text="Optional Filters: ").grid(row=1, columnspan=2)
tk.Label(root, text="City of your location: ").grid(row=2)
tk.Label(root, text="Number of locations needed: ").grid(row=3)
tk.Label(root, text="Latitude of your location: ").grid(row=4)
tk.Label(root, text="Longitude of your location: ").grid(row=5)

options = [
    "Flu Shot",
    "Flu Shot (Egg free)",
    "Flu Shot (65+, high-dose or adjuvanted)",
    "Flu Nasal Spray",
]
clicked = tk.StringVar()
clicked.set("Choose Vaccine")
drop = tk.OptionMenu(root, clicked, *options)

textbox1 = tk.Entry(root)
textbox2 = tk.Entry(root)
textbox3 = tk.Entry(root)
textbox4 = tk.Entry(root)
drop.grid(row=0, column=1)
textbox1.grid(row=2, column=1)
textbox2.grid(row=3, column=1)
textbox3.grid(row=4, column=1)
textbox4.grid(row=5, column=1)

button = tk.Button(
    root, text="Get Information", command=lambda: display_text()
)
clean_button = tk.Button(
    root, text="Clear Text Box", command=lambda: clean_up()
)

displaybox = tk.Text(root)

button.grid(row=6, columnspan=2)
clean_button.grid(row=7, columnspan=2)
displaybox.grid(row=8, columnspan=2)


def format_output(result: list[tuple[str]]) -> str:
    """Format the output."""
    count = 1

    s = ""

    for info in result:
        s += "Option " + str(count) + ":\n"
        s += "\tProvider Name: " + info[0] + "\n"
        s += (
            "\tAddress: "
            + info[1]  # type: ignore
            + ", "
            + info[2]  # type: ignore
            + ", "
            + info[3]  # type: ignore
            + ", "
            + info[4]  # type: ignore
            + "\n"
        )
        s += "\tWebsite: " + info[5] + "\n"  # type: ignore
        s += "\tLatitude: " + info[6] + "\t"  # type: ignore
        s += "Longitude: " + info[7] + "\n"  # type: ignore
        count += 1

    return s


def display_text() -> None:
    """Display the text."""
    lab_info = Flu_info("Flu_Vaccines_Provider_NC.db")
    text0 = clicked.get()
    text1 = textbox1.get()
    text2 = textbox2.get()
    text3 = textbox3.get()
    text4 = textbox4.get()
    if text0 == "Choose Vaccine":
        ll = "Please select the vaccine you want to check."
    elif len(text3) != 0 and len(text4) != 0:
        ll = format_output(lab_info.getInfoByPosition(text3, text4, text0))
    elif len(text3) != 0 or len(text4) != 0:
        ll = "Please enter the full location info!"
    elif len(text2) == 0 and len(text1) == 0:
        ll = format_output(lab_info.getLocationByVaccineName(text0))
    elif len(text2) != 0 and len(text1) != 0:
        ll = format_output(
            lab_info.getLimitedLocationByCityAndVaccineName(
                text1, text0, int(text2)
            )
        )
    elif len(text1) == 0:
        ll = format_output(
            lab_info.getLimitedLocationByVaccineName(text0, int(text2))
        )
    else:
        ll = format_output(
            lab_info.getLocationByCityAndVaccineName(text1, text0)
        )

    displaybox.insert(tk.END, ll)


def clean_up() -> None:
    """Clean up the text."""
    clicked.set("Choose Vaccine")
    textbox1.delete(0, tk.END)
    textbox2.delete(0, tk.END)
    textbox3.delete(0, tk.END)
    textbox4.delete(0, tk.END)
    displaybox.delete("1.0", tk.END)


root.mainloop()
