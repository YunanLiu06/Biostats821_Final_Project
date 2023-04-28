"""Prepossessing module."""
import pandas as pd
import sqlite3
from typing import Any


class Preprocessing:
    """Preprocessing class for the data."""

    def __init__(self, data_path: str) -> None:
        """Initialize the data."""
        self.data_path = data_path
        self.data = pd.read_csv(self.data_path, low_memory=False)

    def drop_columns(self, columns: list[Any]) -> None:
        """Drop columns from the dataset that are not needed."""
        self.data = self.data.drop(columns, axis=1)

    def drop_duplicates(self) -> None:
        """Drop duplicates from the dataset."""
        self.data = self.data.drop_duplicates()

    def fill_na(self, columns: list[Any], value: str) -> None:
        """Fill the missing values with a value."""
        for i in columns:
            self.data[i] = self.data[i].fillna(value)

    def combine_opening_hours(self) -> None:
        """Combine the opening hours into one column."""
        # combine opening hours
        self.data["sunday_hours"] = (
            "sunday_hours:  " + self.data["sunday_hours"].astype(str) + "  |  "
        )
        self.data["monday_hours"] = (
            "monday_hours:  " + self.data["monday_hours"].astype(str) + "  |  "
        )
        self.data["tuesday_hours"] = (
            "tuesday_hours:  "
            + self.data["tuesday_hours"].astype(str)
            + "  |  "
        )
        self.data["wednesday_hours"] = (
            "wednesday_hours:  "
            + self.data["wednesday_hours"].astype(str)
            + "  |  "
        )
        self.data["thursday_hours"] = (
            "thursday_hours:  "
            + self.data["thursday_hours"].astype(str)
            + "  |  "
        )
        self.data["friday_hours"] = (
            "friday_hours:  " + self.data["friday_hours"].astype(str) + "  |  "
        )
        self.data["saturday_hours"] = "saturday_hours:  " + self.data[
            "saturday_hours"
        ].astype(str)
        # combine the hours into one column
        self.data["opening_hours"] = (
            self.data["sunday_hours"]
            + self.data["monday_hours"]
            + self.data["tuesday_hours"]
            + self.data["wednesday_hours"]
            + self.data["thursday_hours"]
            + self.data["friday_hours"]
            + self.data["saturday_hours"]
        )

    def format_phone_number(self, column_name: str) -> None:
        """Format the phone number column."""
        self.data[column_name] = (
            self.data[column_name]
            .str.extractall(r"(\d)")
            .unstack()
            .apply(lambda x: "".join(x), axis=1)
        )
        self.data[column_name] = self.data[column_name].str.replace(
            r"(\d{3})(\d{3})(\d{4})", r"\1-\2-\3", regex=True
        )

    def subset_data(self, column_name: str, value: str) -> pd.DataFrame:
        """Subset the data based on a column name and value."""
        self.data = self.data.loc[self.data[column_name] == value, :]
        subset_data = self.data
        return subset_data

    def save_data(self, file_name: str) -> pd.DataFrame:
        """Save the data to a csv file."""
        final_data = self.data.to_csv(file_name, index=False)
        return final_data


def make_database(csv_path: str, db_path: str) -> None:
    """Make a database for the data."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Vaccines")

    # create a table
    cursor.execute(
        """CREATE TABLE Vaccines (
    guid VARCHAR, phone_number VARCHAR, provider_name VARCHAR,
    street_address1 VARCHAR, city VARCHAR, state VARCHAR,
    zip VARCHAR, website VARCHAR, pre_sreening_required VARCHAR,
    insurance_accepted VARCHAR, walkins_accepted VARCHAR,
    provider_notes VARCHAR, searchable_name VARCHAR, in_stock VARCHAR,
    quantity_last_updated VARCHAR, latitude VARCHAR, longitude VARCHAR,
    hours VARCHAR)"""
    )

    # insert data into the table
    with open(csv_path, "r") as f:
        next(f)  # Skip the header row.
        for line in f:
            vaccines_line = line.strip().split(",")
            cursor.execute(
                "INSERT INTO Vaccines VALUES \
                (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                vaccines_line[0:18],
            )

    connection.commit()
    connection.close()
