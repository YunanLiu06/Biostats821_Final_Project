"""Test utilities for pytest."""


def build_sample_db() -> None:
    """Build a sample database for testing."""
    import sqlite3
    import os

    connection = sqlite3.connect("sampleDB.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Vaccines")
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
    with open("test_make_database.csv", "r") as f:
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


def del_db() -> None:
    """Delete the sample database."""
    import os
    import glob

    db_files = glob.glob("*.db")
    for file in db_files:
        os.remove(file)
