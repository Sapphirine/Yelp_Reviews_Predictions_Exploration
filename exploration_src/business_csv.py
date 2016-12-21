import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

src_dir = ["../json/yelp_academic_dataset_uk_restaurants.json",
           "../json/yelp_academic_dataset_canada_restaurants.json",
           "../json/yelp_academic_dataset_germany_restaurants.json",
           "../json/yelp_academic_dataset_usa_restaurants.json"]

des_dir = ["../csv/yelp_academic_dataset_uk_restaurants.csv",
           "../csv/yelp_academic_dataset_canada_restaurants.csv",
           "../csv/yelp_academic_dataset_germany_restaurants.csv",
           "../csv/yelp_academic_dataset_usa_restaurants.csv"]

for i in range(4):
    f = open(src_dir[i], "r")
    g = open(des_dir[i], "wb+")
    x = csv.writer(g, delimiter=',', quotechar="\"", quoting=csv.QUOTE_NONNUMERIC, lineterminator='\r\n')
    x.writerow(["name", "business_id", "categories", "city", "state", "review_count", "stars", "Take-out",
                "Caters", "Noise Level", "Takes Reservations", "Delivery", "Has TV", "Outdoor Seating", "Attire", "Alcohol",
                "Waiter Service", "Accepts Credit Cards", "Good for Kids", "Good For Groups", "Price Range", "Wi-Fi",
                "Parking_garage", "Parking_street", "Parking_validated", "Parking_lot", "Parking_valet", "good_for_dessert",
                "good_for_latenight", "good_for_lunch", "good_for_dinner", "good_for_brunch", "good_for_breakfast",
                "romantic", "intimate", "classy", "hipster", "divey", "touristy", "trendy", "upscale", "casual", "Mon_open",
                "Mon_close", "Tue_open", "Tue_close", "Wed_open", "Wed_close", "Thu_open", "Thu_close", "Fri_open",
                "Fri_close", "Sat_open", "Sat_close", "Sun_open", "Sun_close"])
    for line in f:
        data = json.loads(line)
        x.writerow([data["name"], data["business_id"], ','.join(data["categories"]), data["city"], data["state"],
                    data["review_count"], data["stars"], data["attributes"].setdefault("Take-out", None),
                    data["attributes"].setdefault("Caters", None), data["attributes"].setdefault("Noise Level", None),
                    data["attributes"].setdefault("Takes Reservations", None),
                    data["attributes"].setdefault("Delivery", None), data["attributes"].setdefault("Has TV", None),
                    data["attributes"].setdefault("Outdoor Seating", None), data["attributes"].setdefault("Attire", None),
                    data["attributes"].setdefault("Alcohol", None), data["attributes"].setdefault("Waiter Service", None),
                    data["attributes"].setdefault("Accepts Credit Cards", None),
                    data["attributes"].setdefault("Good for Kids", None),
                    data["attributes"].setdefault("Good For Groups", None),
                    data["attributes"].setdefault("Price Range", None), data["attributes"].setdefault("Wi-Fi", None),
                    data["attributes"].setdefault("Parking", {}).setdefault("garage", None),
                    data["attributes"].setdefault("Parking", {}).setdefault("street", None),
                    data["attributes"].setdefault("Parking", {}).setdefault("validated", None),
                    data["attributes"].setdefault("Parking", {}).setdefault("lot", None),
                    data["attributes"].setdefault("Parking", {}).setdefault("valet", None),
                    data["attributes"].setdefault("Good For", {}).setdefault("dessert", None),
                    data["attributes"].setdefault("Good For", {}).setdefault("latenight", None),
                    data["attributes"].setdefault("Good For", {}).setdefault("lunch", None),
                    data["attributes"].setdefault("Good For", {}).setdefault("dinner", None),
                    data["attributes"].setdefault("Good For", {}).setdefault("brunch", None),
                    data["attributes"].setdefault("Good For", {}).setdefault("breakfast", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("romantic", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("intimate", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("classy", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("hipster", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("divey", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("touristy", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("trendy", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("upscale", None),
                    data["attributes"].setdefault("Ambience", {}).setdefault("casual", None),
                    data["hours"].setdefault("Monday", {}).setdefault("open", None),
                    data["hours"].setdefault("Monday", {}).setdefault("close", None),
                    data["hours"].setdefault("Tuesday", {}).setdefault("open", None),
                    data["hours"].setdefault("Tuesday", {}).setdefault("close", None),
                    data["hours"].setdefault("Wednesday", {}).setdefault("open", None),
                    data["hours"].setdefault("Wednesday", {}).setdefault("close", None),
                    data["hours"].setdefault("Thursday", {}).setdefault("open", None),
                    data["hours"].setdefault("Thursday", {}).setdefault("close", None),
                    data["hours"].setdefault("Friday", {}).setdefault("open", None),
                    data["hours"].setdefault("Friday", {}).setdefault("close", None),
                    data["hours"].setdefault("Saturday", {}).setdefault("open", None),
                    data["hours"].setdefault("Saturday", {}).setdefault("close", None),
                    data["hours"].setdefault("Sunday", {}).setdefault("open", None),
                    data["hours"].setdefault("Sunday", {}).setdefault("close", None),
                    ])
    # abandon data["attributes"]["Drive-Thru", "Music"], data["open], "type", "neighbourhoods", "longitude", "latitude"
    f.close()
    g.close()

