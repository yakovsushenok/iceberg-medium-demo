from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json import LetterCase, dataclass_json


@dataclass_json
@dataclass
class Keys:
    person_name: str
    sort_key: str


class Maintenance:
    oil_changes: List[str]


class Car:
    make: str
    mode: str
    maintenance: Maintenance


class NewImage:
    person_name: str
    sort_key: str
    cars: List[Car]


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class DynamoDB:
    approximate_creation_date_time: float
    keys: Keys
    sequence_number: str
    size_bytes: int
    new_image: Optional[NewImage] = None
    old_image: Optional[NewImage] = None
