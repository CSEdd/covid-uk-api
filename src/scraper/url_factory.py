from datetime import datetime
from scraper.types import UrlValues

URL = "https://api.coronavirus.data.gov.uk/v2/data?areaType=overview"


def construct_url_object(format: str, metrics: list[str], date: datetime) -> UrlValues:
    return UrlValues(format=format, metrics=metrics, date=date)


def construct_url(url_obj: UrlValues) -> str:
    # Base URL
    url = f"{URL}"

    # Add Metrics
    for metric in url_obj.metrics:
        url += f"&metric={metric}"

    # Add Data Format
    url += f"&format={url_obj.format}"

    # Add Release Date
    url += f"&release={url_obj.date.strftime('%Y-%m-%d')}"

    return url


if __name__ == "__main__":
    pass
