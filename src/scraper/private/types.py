from pydantic import BaseModel, ValidationError, validator
from typing import List, ValuesView
from datetime import datetime

FORMATS = ["csv", "json", "xml", "jsonl"]

METRICS = [
    "capacityPillarFour",
    "capacityPillarOne",
    "capacityPillarOneTwo",
    "capacityPillarThree",
    "capacityPillarTwo",
    "covidOccupiedMVBeds",
    "cumAdmissions",
    "cumAntibodyTestsByPublishDate",
    "cumCasesByPublishDate",
    "cumCasesByPublishDateRate",
]


class ApiRequestValues(BaseModel):
    format: str
    metrics: List[str]
    date: datetime

    @validator("format")
    def check_format(cls, v):
        assert v in FORMATS, f"{v} is not a valid format"
        return v

    @validator("metrics", each_item=True)
    def check_metrics(cls, v):
        assert v in METRICS, f"{v} is not a valid metric"
        return v
