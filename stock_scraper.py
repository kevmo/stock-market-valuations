import csv
import requests


URL = "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"

def request_nasdaq_100_data():
    """Get the current data for the NASDAQ 100"""
    r = requests.get(URL)
    r.endcoding = 'csv'
    data = r.text

    return data


def get_stock_data():
    stocks = {}
    data = request_nasdaq_100_data()

    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        SYMBL = line.get('Symbol')
        stocks[SYMBL] = {
            'last_sale': line.get('lastsale'),
            'name': line.get('Name'),
            'symbol': line.get('Symbol'),
            'share_volume': line.get('share_volume'),
            'pctchange': line.get('pctchange'),
            'Nasdaq100_points': line.get('Nasdaq100_points'),
            'netchange': line.get('netchange')
        }

    return stocks
