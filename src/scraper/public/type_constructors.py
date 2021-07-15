from scraper.private.types import *
from datetime import datetime


def create_api_request_values(format: str, metrics: list[str], date: datetime) -> ApiRequestValues:
    return ApiRequestValues(format=format, metrics=metrics, date=date)
