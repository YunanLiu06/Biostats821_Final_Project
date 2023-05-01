"""Test for get_info.py."""
import pytest
import sqlite3
from get_info import Flu_info
from test_utility import build_sample_db, del_db

# build a sample database for testing
build_sample_db()

# initialize the class
test = Flu_info("sampleDB.db")


def test_getInfoByPosition() -> None:
    # test = Flu_info("sampleDB.db")
    nearest_position = test.getInfoByPosition("35", "-78", "Flu Shot")[0]
    assert (
        nearest_position[0] == "Cape Fear LTC Pharmacy LLC #1"
    ), "Incorrect data"
    assert nearest_position[1] == "185 Pine State St", "Incorrect data"
    assert nearest_position[2] == "Lillington", "Incorrect data"
    assert nearest_position[3] == "NC", "Incorrect data"
    assert nearest_position[4] == "27546", "Incorrect data"
    assert nearest_position[5] == "Not Available", "Incorrect data"
    assert nearest_position[6] == "35.422599", "Incorrect data"
    assert nearest_position[7] == "-78.805035", "Incorrect data"


def test_getLocationByVaccineName() -> None:
    result_location = test.getLocationByVaccineName("Flu Shot")
    assert len(result_location) == 3, "Incorrect data"
    print(result_location[0])
    assert result_location[0] == (
        "Thomas Drugs #3438365",
        "7917 E OAK ISLAND DR",
        "Oak Island",
        "NC",
        "28465",
        "Not Available",
        "33.908618",
        "-78.085272",
    ), "Incorrect data"
    assert result_location[2] == (
        "Cape Fear LTC Pharmacy LLC #1",
        "185 Pine State St",
        "Lillington",
        "NC",
        "27546",
        "Not Available",
        "35.422599",
        "-78.805035",
    ), "Incorrect data"


def test_getLocationByCityAndVaccineName() -> None:
    result_location = test.getLocationByCityAndVaccineName(
        "Oak Island", "Flu Shot"
    )
    assert len(result_location) == 2, "Incorrect data"
    assert result_location[0] == (
        "Thomas Drugs #3438365",
        "7917 E OAK ISLAND DR",
        "Oak Island",
        "NC",
        "28465",
        "Not Available",
        "33.908618",
        "-78.085272",
    ), "Incorrect data"


def test_getLimitedLocationByVaccineName() -> None:
    result_location = test.getLimitedLocationByVaccineName("Flu Shot", 1)
    assert len(result_location) == 1, "Incorrect data"
    assert result_location[0] == (
        "Thomas Drugs #3438365",
        "7917 E OAK ISLAND DR",
        "Oak Island",
        "NC",
        "28465",
        "Not Available",
        "33.908618",
        "-78.085272",
    ), "Incorrect data"


def test_getLimitedLocationByCityAndVaccineName() -> None:
    result_location = test.getLimitedLocationByCityAndVaccineName(
        "Oak Island", "Flu Shot", 1
    )
    assert len(result_location) == 1, "Incorrect data"
    assert result_location[0] == (
        "Thomas Drugs #3438365",
        "7917 E OAK ISLAND DR",
        "Oak Island",
        "NC",
        "28465",
        "Not Available",
        "33.908618",
        "-78.085272",
    ), "Incorrect data"
