import datetime
import pytest

from src.scraper.url_factory import construct_url

def test_simple_build():
    date = datetime.datetime(2021, 7, 14)
    url = construct_url("csv", ["capacityPillarFour", "capacityPillarOne"], date)
    assert url == 'https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=capacityPillarFour&metric=capacityPillarOne&format=csv&release=2021-07-14'
