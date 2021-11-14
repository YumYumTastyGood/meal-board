from typing import Union
from database.interfaces.School import SchoolInfo, Location
import re


def get_school_list(location: str, school: str) -> list:
    schools = SchoolInfo.objects.filter(
        region_code=location, school_name__icontains=school
    )
    return schools


def get_location_list() -> list:
    locations = Location.objects()
    return locations
