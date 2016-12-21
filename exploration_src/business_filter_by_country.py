import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f = open("../json/yelp_academic_dataset_business.json", "r")
g = open("../json/yelp_academic_dataset_restaurants.json", "w")

business_id = []
for line in f:
    data = json.loads(line)
    if "Restaurants" in data["categories"]:
        business_id.append(data["business_id"])
        json.dump(data, g)
        g.write('\n')  # add an '\n' after each json object
g.close()

f.close()

# -----------------------------------------------------------------------------
f_res = open("../json/yelp_academic_dataset_restaurants.json", "r")

# json file for restaurants in US
g_usa = open("../json/yelp_academic_dataset_usa_restaurants.json", "w")

for line in f_res:
    data = json.loads(line)
    if data["state"] in ["PA", "NC", "SC", "WI", "IL", "AZ", "NV", "TX", "AK", "FL", "NM"]:
        json.dump(data, g_usa)
        g_usa.write('\n')  # add an '\n' after each json object

g_usa.close()

f_res.close()

# -----------------------------------------------------------------------
f_res = open("../json/yelp_academic_dataset_restaurants.json", "r")
# json file for restaurants in Canada
g_can = open("../json/yelp_academic_dataset_canada_restaurants.json", "w")

for line in f_res:
    data = json.loads(line)
    if data["state"] in ["QC", "ON"]:
        json.dump(data, g_can)
        g_can.write('\n')  # add an '\n' after each json object

g_can.close()

f_res.close()

# --------------------------------------------------------------------------
f_res = open("../json/yelp_academic_dataset_restaurants.json", "r")
# json file for restaurants in UK
g_uk = open("../json/yelp_academic_dataset_uk_restaurants.json", "w")

for line in f_res:
    data = json.loads(line)
    if data["state"] in ["EDH", "MLN", "FIF", "ELN", "KHL"]:
        json.dump(data, g_uk)
        g_uk.write('\n')  # add an '\n' after each json object

g_uk.close()

f_res.close()

# -------------------------------------------------------------------------
f_res = open("../json/yelp_academic_dataset_restaurants.json", "r")
# json file for restaurants in Germany
g_ger = open("../json/yelp_academic_dataset_germany_restaurants.json", "w")

for line in f_res:
    data = json.loads(line)
    if data["state"] in ["BW", "RP", "NW"]:
        json.dump(data, g_ger)
        g_ger.write('\n')  # add an '\n' after each json object

g_ger.close()

f_res.close()


# filter review

f_review = open("../json/yelp_academic_dataset_review.json", "r")
g_review = open("../json/yelp_academic_dataset_review_restaurant.json", "w")

for line in f_review:
    data = json.loads(line)
    if data["business_id"] in business_id:
        json.dump(data, g_review)
        g_review.write('\n')  # add an '\n' after each json object
g_review.close()

f_review.close()




