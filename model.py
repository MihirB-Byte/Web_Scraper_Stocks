import requests
from bs4 import BeautifulSoup


class Model:
    def __init__(self):
        self.data = {}

    def fetch_data(self, stock_code):
        # fetch the data from Yahoo Finance using the stock code
        url = f"https://finance.yahoo.com/quote/{stock_code}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        data = {}

        # extract the relevant data from the page
        data["price"] = soup.find("span", class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)").text
        data["volume"] = soup.find("td", class_="Ta(end) Fw(b) Lh(14px)").text
        data["market_cap"] = soup.find("td", class_="Py(10px) Ta(end)").text

        return data