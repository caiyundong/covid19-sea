from datetime import datetime, timedelta
import requests
import re
from bs4 import BeautifulSoup as bs
import time


def previous_date(current_date, days=1):
    """
    Return the previous_date
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

    # pattern = r"\{\{Medical cases chart/Row\|(\d+?-\d+?-\d+?)\|(|\d*?)\|(|\d*?)\|(|\d*?)\|\|\|(|\d*?)\|.+?\|(|\d*?)\|.+?\}\}"
    pattern = r"\{\{Medical cases chart/Row\|(\d+?-\d+?-\d+?)\|(|\d*?)\|(|\d*?)\|(|\d*?)\|.+?\}\}"
    results = re.findall(pattern, soup.textarea.text, re.MULTILINE)
    print(results)

    for result in results:
        dt = result[0]
        death = 0 if result[1] == '' else int(result[1])
        cued = 0 if result[2] == '' else int(result[2])
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
        print(result_json, {"country": country, "date": dt} )
        daily_collection.update({"country": country, "date": dt}, {'$set': result_json}, upsert=True)
        total_records[dt] = result_json