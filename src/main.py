from datetime import datetime


from scraper.url_factory import construct_url, construct_url_object


def main():
    date = datetime(2021, 7, 14)
    url_obj = construct_url_object(
        "csv", ["capacityPillarFour", "capacityPillarOne"], date
    )
    url = construct_url(url_obj)
    print(url)


main()
