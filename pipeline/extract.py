"""Script to extract the data from url."""

from os.path import exists
from os import mkdir
import urllib.request

DATA_API_ENDPOINT = "https://data.nasa.gov/resource/eva.json"
FILEPATH = "data/nasa_eva_records.json"


def download_nasa_eva_data() -> None:
    """Downloads the NASA EVA dataset as a csv from the API and 
    saves it locally."""
    make_download_folder()
    urllib.request.urlretrieve(DATA_API_ENDPOINT, FILEPATH)


def make_download_folder() -> None:
    """Checks that a download folder has been created, and
    if not, creates it."""
    if not exists("data"):
        mkdir("data")


if __name__ == "__main__":
    download_nasa_eva_data()
