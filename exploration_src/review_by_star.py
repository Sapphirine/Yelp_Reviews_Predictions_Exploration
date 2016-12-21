import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

src_dir = ["../csv/review_uk.csv",
           "../csv/review_usa.csv",
           "../csv/review_can.csv",
           "../csv/review_ger.csv"]

des_dir_5 = ["../review-star/uk-review-5.txt",
             "../review-star/usa-review-5.txt",
             "../review-star/can-review-5.txt",
             "../review-star/ger-review-5.txt"]

des_dir_4 = ["../review-star/uk-review-4.txt",
             "../review-star/usa-review-4.txt",
             "../review-star/can-review-4.txt",
             "../review-star/ger-review-4.txt"]

des_dir_3 = ["../review-star/uk-review-3.txt",
             "../review-star/usa-review-3.txt",
             "../review-star/can-review-3.txt",
             "../review-star/ger-review-3.txt"]

des_dir_2 = ["../review-star/uk-review-2.txt",
             "../review-star/usa-review-2.txt",
             "../review-star/can-review-2.txt",
             "../review-star/ger-review-2.txt"]

des_dir_1 = ["../review-star/uk-review-1.txt",
             "../review-star/usa-review-1.txt",
             "../review-star/can-review-1.txt",
             "../review-star/ger-review-1.txt"]



for i in range(4):
    f = open(src_dir[i], "r")
    g5 = open(des_dir_5[i], "wb+")
    g4 = open(des_dir_4[i], "wb+")
    g3 = open(des_dir_3[i], "wb+")
    g2 = open(des_dir_2[i], "wb+")
    g1 = open(des_dir_1[i], "wb+")
    review_reader = csv.reader(f)
    for row in review_reader:
        if row[-2] == "5":
            g5.write(row[-3])
        elif row[-2] == "4":
            g4.write(row[-3])
        elif row[-2] == "3":
            g3.write(row[-3])
        elif row[-2] == "2":
            g2.write(row[-3])
        elif row[-2] == "1":
            g1.write(row[-3])

    f.close()
    g5.close()
    g4.close()
    g3.close()
    g2.close()
    g1.close()