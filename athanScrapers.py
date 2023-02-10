import datetime
from abc import ABC, abstractmethod

import pandas as pd
import requests
from bs4 import BeautifulSoup


class AthanScraper(ABC):
    URL: str

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    @abstractmethod
    def scrape_athan_page(self, response, date: datetime.datetime) -> pd.Series:
        """Scrape the athan data from the page using the response provided and return a series with athan name as
        index, and athan time as datetime."""
        pass

    def get_athan_times(self, date: datetime.datetime) -> pd.Series:
        try:
            response: requests.Response = requests.get(url=self.URL, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            return self.scrape_athan_page(response, date)


class MadridIslamicCenter(AthanScraper):
    URL = "https://centro-islamico.com/"

    def scrape_athan_page(self, response, date: datetime.datetime) -> pd.Series:
        soup = BeautifulSoup(response.content, "html5lib")

        athan = ["Fajr", "Duhr", "Asr", "Maghrib", "Ishaa"]

        prayers_table = soup.find_all("span", {"class": "dpt_start"})

        athan_time = []

        for row in prayers_table:
            time = datetime.datetime.strptime(row.text.lower(), "%I:%M %p")
            time = datetime.datetime(date.year, date.month, date.day, time.hour, time.minute)
            athan_time.append(time)

        return pd.Series(athan_time, index=athan)
