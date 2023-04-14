"""Unit tests for the Preprocessing.py file"""
import pytest
from Preprocessing import Preprocessing, make_database
import sqlite3

test_data = Preprocessing("test.csv")


def test_drop_columns() -> None:
    """Test the drop_columns function"""
    test_data.drop_columns(["longitude", "latitude"])
    with pytest.raises(KeyError):
        test_data.data["latitude"]
        test_data.data["longitude"]


def test_drop_duplicates() -> None:
    """Test the drop_duplicates function"""
    test_data.drop_duplicates()
    assert test_data.data.duplicated().sum() == 0


def test_fill_na() -> None:
    """Test the fill_na function"""
    for i in test_data.data.columns:
        test_data.fill_na([i], "Not Available")
        assert test_data.data[i].isna().sum() == 0


def test_combine_opening_hours() -> None:
    """Test the combine_opening_hours function"""
    test_data.combine_opening_hours()
    assert (
        test_data.data["opening_hours"][0]
        == "sunday_hours:  Not Available  |  monday_hours:  8:00 AM - 5:00 PM  |  "
        + "tuesday_hours:  8:00 AM - 5:00 PM  |  wednesday_hours:  8:00 AM - 5:00 PM  |  "
        + "thursday_hours:  8:00 AM - 5:00 PM  |  friday_hours:  8:00 AM - 5:00 PM  |  "
        + "saturday_hours:  Not Available"
    )


def test_format_phone_number() -> None:
    """Test the format_phone_number function"""
    test_data.format_phone_number("loc_phone")
    assert test_data.data["loc_phone"][0] == "580-924-4285"


def test_subset_data() -> None:
    """Test the subset_data function"""
    test_data.subset_data("loc_admin_state", "NY")
    for i in test_data.data["loc_admin_state"]:
        assert i == "NY"
