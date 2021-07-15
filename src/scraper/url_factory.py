from datetime import datetime

URL = "https://api.coronavirus.data.gov.uk/v2/data?areaType=overview"

METRICS = [
    "capacityPillerFour",
    "capacityPillerOne",
    "capacityPillerOneTwo",
    "capacityPillerThree",
    "capacityPillerTwo",
]


def construct_url(format: str, metrics: list[str], date: datetime) -> str:
    # Base URL
    url = f"{URL}"

    # Add Metrics
    for metric in metrics:
        url += f"&metric={metric}"

    # Add Data Format
    url += f"&format={format}"

    # Add Release Date
    url += f"&release={date.strftime('%Y-%m-%d')}"

    return url


if __name__ == "__main__":
    pass
