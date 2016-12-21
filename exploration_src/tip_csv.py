import json
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8')

src_dir_1 = "../json/yelp_academic_dataset_user.json"

src_dir_2 = ["../json/yelp_academic_dataset_usa_restaurants.json",
             "../json/yelp_academic_dataset_uk_restaurants.json",
             "../json/yelp_academic_dataset_canada_restaurants.json",
             "../json/yelp_academic_dataset_germany_restaurants.json"]

src_dir_3 = ["../json/yelp_academic_dataset_usa_tip.json",
             "../json/yelp_academic_dataset_uk_tip.json",
             "../json/yelp_academic_dataset_canada_tip.json",
             "../json/yelp_academic_dataset_germany_tip.json"]

des_dir = ["../csv/tip_usa.csv",
           "../csv/tip_uk.csv",
           "../csv/tip_can.csv",
           "../csv/tip_ger.csv"]

for i in range(4):
    f = open(src_dir_1, "r")
    g = open(src_dir_2[i], "r")
    h = open(src_dir_3[i], "r")
    j = open(des_dir[i], "wb+")

    user = {}
    restaurants ={}

    for line in f:
        data = json.loads(line)
        user[data["user_id"]] = data["name"]

    for line in g:
        data = json.loads(line)
        restaurants[data["business_id"]] = data["name"]


    x = csv.writer(j, delimiter=',', quotechar="\"", quoting=csv.QUOTE_NONNUMERIC, lineterminator='\r\n')
    x.writerow(["user_id", "user_name", "restaurant_id", "restaurant_name", "text", "likes", "date"])
    for line in h:
        data = json.loads(line)
        x.writerow([data["user_id"], user[data["user_id"]], data["business_id"],
                    restaurants[data["business_id"]], data["text"].replace('\n', ''), data["likes"], data["date"]])

    f.close()
    g.close()
    h.close()
    j.close()