from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json import LetterCase, dataclass_json


@dataclass_json
@dataclass
class Keys:
    person_name: str
    sort_key: str


@dataclass_json
@dataclass
class Maintenance:
    oil_changes: List[str]


@dataclass_json
@dataclass
class Car:
    make: str
    maintenance: Maintenance
    model: str


@dataclass_json
@dataclass
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
