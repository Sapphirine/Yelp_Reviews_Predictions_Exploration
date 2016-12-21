import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# user.csv
f = open("json/yelp_academic_dataset_user.json", "r")
g = open("csv/yelp_academic_dataset_user.csv", "wb+")
x = csv.writer(g, delimiter=',', quotechar="\"", quoting=csv.QUOTE_NONNUMERIC, lineterminator='\r\n')
x.writerow(["name", "user_id", "yelping_since", "votes_funny", "votes_useful", "votes_cool", "review_count",
            "friends_count", "fans", "average_stars"])
for line in f:
    data = json.loads(line)
    x.writerow([data["name"], data["user_id"], data["yelping_since"], data["votes"]["funny"], data["votes"]["useful"],
                data["votes"]["cool"], data["review_count"], len(data["friends"]), data["fans"], data["average_stars"]])
f.close()
g.close()