import logging
from pymongo import MongoClient
import redis
from common import *
import time

# setup the mongodb client
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',)
try:
    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client.covid19
    daily_collection = db['daily']
    case_collection = db['case']        # only Singapore now
except Exception as err:
    logging.log("Failed to connect to mongodb")
    time.sleep(5)

# setup redis
redis_client = redis.StrictRedis("localhost")


if __name__ == "__main__":
    logging.info("Start the crawl")

    wikipedia_addresses = {
        'Malaysia': "https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Malaysia_medical_cases_chart&action=edit",
        'Indonesia': "https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Indonesia_medical_cases_chart&action=edit",
        'Thailand': 'https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Thailand_medical_cases_chart&action=edit',
        'Vietnam': 'https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Vietnam_medical_cases_chart&action=edit',
        'Philippines': 'https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Philippines_medical_cases_chart&action=edit',
        'Burnei': 'https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Brunei_medical_cases_chart&action=edit',
        'Singapore': 'https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Singapore_medical_cases_chart&action=edit',
    }

    for country, url in wikipedia_addresses.items():
        logging.info("Country: " + country + " / URL: " + url)

        # parse the data from wikipedia
        parse_wikipedia(url=url, country=country, daily_collection=daily_collection)

        # export the data into json and csv
        export_to_file(country=country, format='all', daily_collection=daily_collection)

    logging.info("End of the crawl")

