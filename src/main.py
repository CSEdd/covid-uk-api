from datetime import datetime


from scraper.public.functions import *
from scraper.public.type_constructors import *


def main():
    date = datetime(2021, 7, 14)
    api_request_values = create_api_request_values(
        "csv", ["capacityPillarFour", "capacityPillarOne"], date
    )
    url = generate_url(api_request_values)
    print(url)


main()
