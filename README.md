# covid19-sea [中文](/research/readme_CN.md#疫情相关资源总结)
![COVID19](https://images.unsplash.com/flagged/photo-1584036561584-b03c19da874c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1778&q=80)
COVID 19 Data and Dashboard for southeast asia (Singapore, Malaysia, Indonesia, Thailand, Vietnam, Philippines, Myanmar, Brunei, Laos, Cambodia, East Timor)


**Todo**

- [x] Crawler to fetch the daily statistics from wikipedia
- [x] Save the latest data into data folder
- [ ] Setup the cronjob to crawl data
- [ ] Provide API to fetch online

# Data Source
* Singapore
   * https://www.moh.gov.sg/covid-19
   * Dashboard (one day delay from realtime data) http://go.gov.sg/covid-19-dashboard
      * **Daily**: https://services6.arcgis.com/LZwBmoXba0zrRap7/arcgis/rest/services/COVID_19_Prod_cumulative/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Date%20asc&resultOffset=0&resultRecordCount=2000&cacheHint=true
      * **All detailed cases**: https://services6.arcgis.com/LZwBmoXba0zrRap7/arcgis/rest/services/COVID_19_Prod_feature/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Case_ID%20asc&resultOffset=0&resultRecordCount=1000&cacheHint=true
* Malaysia - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Malaysia
* Indonesia - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Indonesia
* Thailand - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Thailand
* Vietnam - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Vietnam
* Philippines - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_Philippines
* Myanmar - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Myanmar 
* Brunei - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Brunei
* Laos - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Laos
* Cambodia - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Cambodia
* East Timor - https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_East_Timor

# Web Server
The web server is build with Flask + Flask-restful.
```
cd web_server
python app.py
```

The available APIs
* List SEA countries
  * http://127.0.0.1:5000/api/countries

* List daily statistics
  * http://127.0.0.1:5000/api/daily/singapore?limit=4

* List the detailed cases (only Singapore available)
  * http://127.0.0.1:5000/api/case/singapore?limit=4


# Database
## Mongodb 
* DB name: covid19
   * Collections
      * daily (daily statistics for all SEA countries)
      * case (only for singapore)
