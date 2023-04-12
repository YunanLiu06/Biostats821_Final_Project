import tkinter as tk
import sqlite3


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create a label and entry widget for the number of rows to display
        self.rows_label = tk.Label(self, text="Number of rows:")
        self.rows_label.grid(row=0, column=0)
        self.rows_entry = tk.Entry(self)
        self.rows_entry.grid(row=0, column=1)

        # create a button widget to browse the database
        self.browse_button = tk.Button(
            self, text="Browse", command=self.browse_database
        )
        self.browse_button.grid(row=1, column=0, columnspan=2)

        # create a label and drop-down menu widget for the flu shot name search
        self.flu_shot_label = tk.Label(self, text="Flu Shot Name:")
        self.flu_shot_label.grid(row=2, column=0)
        self.flu_shot_var = tk.StringVar(self)
        self.flu_shot_var.set("Flu Shot")
        self.flu_shot_dropdown = tk.OptionMenu(
            self,
            self.flu_shot_var,
            "Flu Shot",
            "Flu Shot (Egg free)",
            "Flu Shot (65+, high-dose or adjuvanted)",
            "Flu Nasal Spray",
        )
        self.flu_shot_dropdown.grid(row=2, column=1)

        # create a label and entry widget for the city search
        self.city_label = tk.Label(self, text="City:")
        self.city_label.grid(row=3, column=0)
        self.city_entry = tk.Entry(self)
        self.city_entry.grid(row=3, column=1)

        # create a button widget to search the database by flu shot name and city
        self.search_button = tk.Button(
            self, text="Search by Flu Shot and City", command=self.search_database
        )
        self.search_button.grid(row=4, column=0, columnspan=2)

        # create a text widget to display the database contents
        self.text = tk.Text(self)
        self.text.grid(row=5, column=0, columnspan=2)

    def browse_database(self):
        # get the number of rows to display from the entry widget
        num_rows = int(self.rows_entry.get())

        # connect to the SQLite database
        conn = sqlite3.connect("Flu_Vaccines_Provider_NC.db")
        c = conn.cursor()

        # execute a SELECT statement to retrieve the requested number of rows
        c.execute("SELECT * FROM Vaccines LIMIT ?", (num_rows,))
        rows = c.fetchall()

        # clear the text widget and insert the retrieved rows
        self.text.delete("1.0", tk.END)
        for row in rows:
            self.text.insert(tk.END, f"{row}\n")

        # close the database connection
        conn.close()

    def search_database(self):
        # get the flu shot name and city to search for from the drop-down menus and entry widget
        search_flu_shot = self.flu_shot_var.get()
        search_city = self.city_entry.get()

        # connect to the SQLite database
        conn = sqlite3.connect("Flu_Vaccines_Provider_NC.db")
        c = conn.cursor()

        # execute a SELECT statement to retrieve the rows with the specified flu shot name and city
        c.execute(
            "SELECT * FROM Vaccines WHERE searchable_name = ? AND city = ? AND in_stock = 'True'",
            (search_flu_shot, search_city),
        )
        rows = c.fetchall()

        # clear the text widget and insert the retrieved rows
        self.text.delete("1.0", tk.END)
        for row in rows:
            self.text.insert(tk.END, f"{row}\n")

        # close the database connection
        conn.close()


# create the main Tkinter window and start the event loop
root = tk.Tk()
app = Application(master=root)
app.mainloop()
