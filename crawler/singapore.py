import requests
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


if __name__ == "__main__":
    logging.info("Start the crawl")

    # crawl the daily statistics
    json_arr = []
    results = requests.get("https://services6.arcgis.com/LZwBmoXba0zrRap7/arcgis/rest/services/COVID_19_Prod_cumulative/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Date%20asc&resultOffset=0&resultRecordCount=2000&cacheHint=true").json()

    for result in results['features']:
        attributes = result['attributes']
        dt = datetime.fromtimestamp(attributes['Date']/1000).strftime("%Y-%m-%d")
        result_json = {
            "country": "Singapore",
            "date": dt,
            "confirmed": attributes['Confirmation_Volume'],
            "confirmed_total": attributes['Confirmation_Total'],
            "discharged": attributes['Discharge_Volume'],
            "discharged_total": attributes['Discharge_Total'],
            "hospitalised": attributes['Dummy'],
            "update_ts": time.time()
        }
        print(result_json)
        json_arr.append(result_json)
        daily_collection.update({"country": "Singapore", "date": dt}, result_json, upsert=True)

    parse_wikipedia(url="https://en.wikipedia.org/w/index.php?title=Template:2019%E2%80%9320_coronavirus_pandemic_data/Malaysia_medical_cases_chart&action=edit", country='Malaysia', daily_collection=daily_collection)

    # export to files
    export_to_file(country='Singapore', format='csv', daily_collection=daily_collection)
    export_to_file(country='Singapore', format='json', daily_collection=daily_collection)

    # crawl the detailed cases
    logging.info("Craw the cases in Singapore")
    detailed_cases = requests.get("https://services6.arcgis.com/LZwBmoXba0zrRap7/arcgis/rest/services/COVID_19_Prod_feature/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Case_ID%20asc&resultOffset=0&resultRecordCount=1000&cacheHint=true").json()
    # print(detailed_cases)
    # print(detailed_cases['features'])
    case_json_arr = []
    for idx, result in enumerate(detailed_cases['features']):
        attributes = result['attributes']
        case_id = attributes['Case_ID']
        cluster = attributes['Cluster']
        current_location = attributes['Current_Lo']
        phi = attributes['PHI']
        imported_o = attributes['Imported_o']
        place = attributes['Place']
        age = attributes['Age']
        gender = attributes['Gender']
        nationality = attributes['Nationalit']
        status = attributes['Status']
        confirmation_date = datetime.fromtimestamp(attributes['Date_of_Co']/1000).strftime("%Y-%m-%d")
        discharged_date = attributes['Date_of_Di']
        region_201 = attributes['Region_201']
        planning_area = attributes['PlanningAr']
        postcode = attributes['POST_CODE']
        longtitude = attributes['LONG']
        latitude = attributes['LAT']
        place_visited = attributes['PLAC_VISTD']
        residence_location = attributes['RES_LOC']

        result_json = {
            "country": "Singapore",
            "case_id": case_id,
            "cluster": cluster,
            "current_location": current_location,
            "phi": phi,
            "imported_o": imported_o,
            "place": place,
            "age": age,
            "gender": gender,
            "nationality": nationality,
            "status": status,
            "confirmation_date": confirmation_date,
            "discharged_date": discharged_date,
            "region_201": region_201,
            "planning_area": planning_area,
            "postcode": postcode,
            "longtitude": longtitude,
            "latitude": latitude,
            "place_visited": place_visited,
            "residence_location": residence_location

        }
        # print(result_json)
        case_json_arr.append(result_json)
        ret = case_collection.update({"country": "Singapore", "case_id": case_id}, {'$set': result_json}, upsert=True)

        if idx == 0:
            logging.info("Process only once")
            total_day = attributes['TOT_COUNT']
            updated_as_dt = attributes['UPD_AS_AT']
            case_pending = attributes['CASE_PENDG']
            case_negative = attributes['CASE_NEGTV']
            confirmed = attributes['Confirmed']
            discharged = attributes['DISCHARGE']
            death = attributes['DEATH']
            suspect_case = attributes['Suspct_Cas']
            total_nonicu = attributes['Tot_NonICU']
            total_icu = attributes['Tot_ICU']
            total_imported = attributes['Tot_Impotd']
            total_local = attributes['Tot_local']
            total_count = attributes['Case_total']
            url = attributes['Prs_rl_URL']

    with open('../data/singapore_cases.json', 'w') as outfile:
        json.dump(case_json_arr, outfile)
