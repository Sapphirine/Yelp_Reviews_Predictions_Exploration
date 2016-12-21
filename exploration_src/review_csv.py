import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

src_dir_1 = "../json/yelp_academic_dataset_user.json"

src_dir_2 = ["../json/yelp_academic_dataset_usa_restaurants.json",
             "../json/yelp_academic_dataset_uk_restaurants.json",
             "../json/yelp_academic_dataset_canada_restaurants.json",
             "../json/yelp_academic_dataset_germany_restaurants.json"]

src_dir_3 = ["../json/yelp_academic_dataset_review_usa.json",
             "../json/yelp_academic_dataset_review_uk.json",
             "../json/yelp_academic_dataset_review_can.json",
             "../json/yelp_academic_dataset_review_ger.json"]

des_dir = ["../csv/review_usa.csv",
           "../csv/review_uk.csv",
           "../csv/review_can.csv",
           "../csv/review_ger.csv"]

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
    x.writerow(["review_id", "user_id", "user_name", "restaurant_id", "restaurant_name", "text", "stars", "date"])
    for line in h:
        data = json.loads(line)
        x.writerow([data["review_id"], data["user_id"], user[data["user_id"]],
                    data["business_id"], restaurants[data["business_id"]],
                    data["text"].replace('\n', ''), data["stars"], data["date"]])

    f.close()
    g.close()
    h.close()
    j.close()
