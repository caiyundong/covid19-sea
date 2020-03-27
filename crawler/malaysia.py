import requests
from bs4 import BeautifulSoup as bs
import logging
import re
from datetime import datetime
from pymongo import MongoClient
import time
import json
import redis
import pandas
from common import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',)
mongo_client = MongoClient('localhost', 27017)
db = mongo_client.covid19

# setup redis
redis_client = redis.StrictRedis("localhost")

daily_collection = db['daily']
case_collection = db['case']        # only Singapore now


def export_to_file(country, format='json', start_date=None, end_date=None, filename=None):
    # fetch the data from the mongodb
    records = list(daily_collection.find({'country': country}, {"_id": 0, "update_ts": 0, "country": 0}))
    print("records are ", records)
    with open(f"../data/{country}_daily.{format}", 'w') as outfile:
        if format == 'json':
            json.dump(records, outfile)
        else:
            print(type(records))
            df = pandas.DataFrame(records)
            print(df)
            csv_content = df.to_csv(index=False, line_terminator='\n')
            outfile.write(csv_content)
            outfile.close()


if __name__ == "__main__":
    logging.info("Start the crawl")

    parse_wikipedia(url="https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Malaysia_medical_cases_chart&action=edit", country='Malaysia', daily_collection=daily_collection)
    # parse_wikipedia(url="https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Indonesia_medical_cases_chart&action=edit", country='Indonesia', daily_collection=daily_collection)


    # export to files
    export_to_file(country='Malaysia', format='csv')
    export_to_file(country='Malaysia', format='json')
    # export_to_file(country='Indonesia', format='csv')
    # export_to_file(country='Indonesia', format='json')
