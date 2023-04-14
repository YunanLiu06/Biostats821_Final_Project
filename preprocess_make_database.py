"""Preprocessing vaccine data and make a database for the vaccine data"""
from Preprocessing import Preprocessing, make_database
import sqlite3

vaccine_data = Preprocessing(
    "/Users/liuxiaoquan/Documents/Vaccines.gov__Flu_vaccinating_provider_locations.csv"
)
vaccine_data.drop_columns(
    ["loc_store_no", "latitude", "longitude", "category", "supply_level"]
)
vaccine_data.combine_opening_hours()
vaccine_data.drop_columns(
    [
        "sunday_hours",
        "monday_hours",
        "tuesday_hours",
        "wednesday_hours",
        "thursday_hours",
        "friday_hours",
        "saturday_hours",
    ]
)
subdata = vaccine_data.subset_data("loc_admin_state", "NC")
vaccine_data.drop_duplicates()
vaccine_data.drop_columns(["loc_admin_street2"])
vaccine_data.fill_na(
    [
        "pre_screen",
        "provider_notes",
        "web_address",
        "insurance_accepted",
        "walkins_accepted",
    ],
    "Not Available",
)
vaccine_data.format_phone_number("loc_phone")

path = "/Users/liuxiaoquan/Documents/GitHub/Biostats821_Final_Project/"
vaccine_data.save_data(path + "data/vaccines_NC.csv")


make_database(
    path + "data/vaccines_NC.csv",
    path + "database/Flu_Vaccines_Provider_NC.db",
)
