import sqlite3
from math import sin, cos, sqrt, atan2, radians


class Flu_info:
    def __init__(self, database: str) -> None:
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()

    def getInfoByPosition(
        self, latitude: str, longitude: str, vaccine_name: str
    ):
        min_dist = float("inf")
        R = 6373.0
        target_latitude = radians(float(latitude))
        target_longitude = radians(float(longitude))

        location_set = self.cursor.execute(
            """ SELECT provider_name, street_address1, city, state, zip, website, latitude, longitude
            FROM Vaccines WHERE searchable_name = ?, in_stock = ?""",
            (
                vaccine_name,
                True,
            ),
        ).fetchall()

        result_location = []

        for location in location_set:
            temp_latitude = radians(float(location[6]))
            temp_longitude = radians(float(location[7]))

            dlon = temp_longitude - target_longitude
            dlat = temp_latitude - target_latitude
            a = (
                sin(dlat / 2) ** 2
                + cos(target_latitude)
                * cos(temp_latitude)
                * sin(dlon / 2) ** 2
            )
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c
            if distance < min_dist:
                result_location.clear()
                result_location.append(location)
            elif distance == min_dist:
                result_location.append(location)

        return result_location

    def getLocationByVaccineName(self, vaccine_name: str):
        location_set = self.cursor.execute(
            """ SELECT provider_name, street_address1, city, state, zip, website, latitude, longitude FROM Vaccines WHERE searchable_name = ? AND in_stock = ?""",
            (
                vaccine_name,
                True,
            ),
        ).fetchall()
        result_location = []
        for location in location_set:
            result_location.append(location)

        return location

    def getLimitedLocationByVaccineName(self, vaccine_name: str, amount: int):
        location_set = self.getLocationByVaccineName(vaccine_name)
        location_selected = []
        for i in range(amount):
            if i >= len(location_set):
                break
            location_selected.append(location_set[i])

        return location_selected


testone = Flu_info("Flu_Vaccines_Provider_NC.db")
testone.getLocationByVaccineName("Flu Shot")
