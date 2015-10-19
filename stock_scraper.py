import csv
import requests


URL = "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"

def get_data():

    r = requests.get(URL)
    r.endcoding = 'csv'
    data = r.text

    for line in csv.DictReader(data.splitlines()):
        print line

    print "HI"
    return {}
