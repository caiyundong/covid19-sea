from datetime import datetime, timedelta
import requests
import re
from bs4 import BeautifulSoup as bs
import time
import json
import pandas


def previous_date(current_date, days=1):
    """
    Return the previous_datef
    :param current_date:
    :return:
    """
    previous_date = datetime.strptime(current_date, "%Y-%m-%d")-timedelta(days=days)
    return previous_date.strftime("%Y-%m-%d")


def parse_wikipedia(url, country, daily_collection):
    total_records = {}

    # only limited data
    # total/death/cued/active
    content = requests.get(url).content
    # print(content)
    soup = bs(content, 'html.parser')
    print(soup.textarea.text)

    if country == 'Singapore':
        pattern = r"(\d+?-\d+?-\d+?);(\d*?);(\d*?);(\d*?);(\d*?);.+?"
    else:
        pattern = r"(\d+?-\d+?-\d+?);(\d*?);(\d*?);(\d*?);.+?"
    results = re.findall(pattern, soup.textarea.text, re.MULTILINE)
    print("results of findall are ", country, results)

    for result in results:
        dt = result[0]
        death = 0 if result[1] == '' else int(result[1])
        cued = 0 if result[2] == '' else int(result[2])
        if country == 'Singapore':
            non_community = 0 if result[3] == '' else int(result[3])
            community = 0 if result[4] == '' else int(result[4])
            total = non_community + community
        else:
            total = int(result[3])
        confirmed = 0
        discharged = 0
        prev_dt = previous_date((dt))
        if prev_dt in total_records:
            confirmed = total - total_records[prev_dt]['confirmed_total']
            discharged = cued - total_records[prev_dt]['discharged_total']

        result_json = {
            "country": country,
            "date": dt,
            "confirmed": int(confirmed),
            "confirmed_total": int(total),
            "discharged": int(discharged),
            "discharged_total": int(cued),
            "death_total": int(death),
            "update_ts": time.time()
        }
        print(result_json, {"country": country, "date": dt})
        daily_collection.update({"country": country, "date": dt}, {'$set': result_json}, upsert=True)
        total_records[dt] = result_json


def export_to_file(country, format='all', start_date=None, end_date=None, filename=None, daily_collection=None):
    # fetch the data from the mongodb
    if not daily_collection:
        raise Exception("Failed to get the mongodb collection")

    records = list(daily_collection.find({'country': country}, {"_id": 0, "update_ts": 0, "country": 0}))
    print("records are ", records)

    filename = f"../data/{country}_daily.{format}"
    if format == 'json':
        with open(filename, 'w') as outfile:
            json.dump(records, outfile, indent=4)
    elif format == 'csv':
        print(type(records))
        df = pandas.DataFrame(records)
        df.to_csv(filename, index=False, line_terminator='\n')
    elif format == 'all':
        filename = f"../data/{country}_daily.json"
        with open(filename, 'w') as outfile:
            json.dump(records, outfile, indent=4)

        filename = f"../data/{country}_daily.csv"
        df = pandas.DataFrame(records)
        df.to_csv(filename, index=False, line_terminator='\n')
    else:
        raise Exception("Invalid export format")