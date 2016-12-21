import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

src_dir_1 = ["../json/yelp_academic_dataset_usa_restaurants.json",
             "../json/yelp_academic_dataset_canada_restaurants.json",
             "../json/yelp_academic_dataset_uk_restaurants.json",
             "../json/yelp_academic_dataset_germany_restaurants.json"]

src_dir_2 = "../json/yelp_academic_dataset_review_restaurant.json"

des_dir = ["../json/yelp_academic_dataset_review_usa.json",
           "../json/yelp_academic_dataset_review_can.json",
           "../json/yelp_academic_dataset_review_uk.json",
           "../json/yelp_academic_dataset_review_ger.json"]

for i in range(4):
    f_review = open(src_dir_1[i], "r")
    business_id_usa = []
    for line in f_review:
        data = json.loads(line)
        business_id_usa.append(data["business_id"])
    f_review.close()

    f1_review = open(src_dir_2, "r")
    g_review = open(des_dir[i], "w")

    for line in f1_review:
        data = json.loads(line)
        if data["business_id"] in business_id_usa:
            json.dump(data, g_review)
            g_review.write('\n')  # add an '\n' after each json object
    g_review.close()

    f1_review.close()