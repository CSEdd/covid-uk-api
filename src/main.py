from datetime import datetime


from scraper.url_factory import construct_url

def main():
    date = datetime(2021, 7, 14)
    url = construct_url("csv", ["capacityPillarFour", "capacityPillarOne"], date)
    print(url)

main()
