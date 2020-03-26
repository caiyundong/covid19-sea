# covid19-sea
COVID 19 Data and Dashboard for southeast asia (Singapore, Malaysia, Indonesia, Thailand, Vietnam, Philippines, Myanmar, Brunei, Laos, Cambodia, East Timor)

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

# Database
## Mongodb 
* DB name: covid19
   * Collections
      * daily (daily statistics for all SEA countries)
      * case (only for singapore)