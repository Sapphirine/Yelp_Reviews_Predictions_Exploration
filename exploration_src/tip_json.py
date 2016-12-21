import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

src_dir_1 = ["../json/yelp_academic_dataset_usa_restaurants.json",
             "../json/yelp_academic_dataset_canada_restaurants.json",
             "../json/yelp_academic_dataset_uk_restaurants.json",
             "../json/yelp_academic_dataset_germany_restaurants.json"]

src_dir_2 = "../json/yelp_academic_dataset_tip.json"

des_dir = ["../json/yelp_academic_dataset_usa_tip.json",
           "../json/yelp_academic_dataset_canada_tip.json",
           "../json/yelp_academic_dataset_uk_tip.json",
           "../json/yelp_academic_dataset_germany_tip.json"]

for i in range(4):
    f = open(src_dir_1[i], "r")
    business_id = []
    for line in f:
        data = json.loads(line)
        business_id.append(data["business_id"])

    f.close()

    f_tip = open(src_dir_2, "r")

    # json file for tip in US
    g = open(des_dir[i], "w")

    for line in f_tip:
        data = json.loads(line)
        if data["business_id"] in business_id:
            json.dump(data, g)
            g.write('\n')  # add an '\n' after each json object

    g.close()

    f_tip.close()