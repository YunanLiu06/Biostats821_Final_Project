"""Test for making database in Preprocessing.py."""
import pytest
import sqlite3
from Preprocessing import make_database
from test_utility import del_db


def test_make_database() -> None:
    """Test for making database in Preprocessing.py."""
    make_database("test_make_database.csv", "test_make_database.db")
    connection = sqlite3.connect("test_make_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Vaccines")
    test1 = cursor.fetchall()[0]
    assert test1[0] == "0a2bcf19-9d62-41e0-b22e-cc6b6c371b63", "Incorrect data"
    assert test1[1] == "910-278-6050", "Incorrect data"
    assert test1[2] == "Thomas Drugs #3438365", "Incorrect data"
    assert test1[3] == "7917 E OAK ISLAND DR", "Incorrect data"
    assert test1[4] == "Oak Island", "Incorrect data"
    assert test1[5] == "NC", "Incorrect data"
    assert test1[6] == "28465", "Incorrect data"
    assert test1[7] == "Not Available", "Incorrect data"
    assert test1[8] == "Not Available", "Incorrect data"
    assert test1[9] == "Not Available", "Incorrect data"
    assert test1[10] == "Not Available", "Incorrect data"
    assert test1[11] == "Not Available", "Incorrect data"
    assert test1[12] == "Flu Shot (Egg free)", "Incorrect data"
    assert test1[13] == "FALSE", "Incorrect data"
    assert test1[14] == "1/9/2023", "Incorrect data"
    assert test1[15] == "33.908618", "Incorrect data"
    assert test1[16] == "-78.085272", "Incorrect data"
    assert (
        test1[17]
        == "sunday_hours:  nan  |  monday_hours:  nan  |  tuesday_hours:  nan"
        "  |  wednesday_hours:  nan  |  thursday_hours:  nan  |  "
        "friday_hours:  nan  |  saturday_hours:  nan"
    ), "Incorrect data"


# delete the database
del_db()
