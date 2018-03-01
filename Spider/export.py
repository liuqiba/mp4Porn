import csv

import pymongo

import os
import io
from io import FileIO
import sys
import requests
DIR = "d:\mp4"
coll = pymongo.MongoClient().sihu.mp4
"""
coll=pymongo.MongoClient().sihu.mp4

with open("XXX.csv","w",newline="") as datacsv:
    csvwriter = csv.writer(datacsv,delimiter=' ',dialect = ("excel"))

    for item in coll.find():
        csvwriter.writerow(item['mp4'])
"""


"""
写txt
"""
with open(os.path.join(DIR,"ddd.txt"),"ab") as f:
    for item in coll.find():
        f.write((item['mp4']+"\n").encode())
        




"""
直接下载
"""
#创建文件夹

"""
if not os.path.exists(DIR):
    os.makedirs(DIR)


for item in coll.find():
    mp4 = requests.get(item['mp4'],timeout = 10).content
    with open(os.path.join(  DIR,"1.mp4"),"ab") as f:
        f.write(mp4)
        break
    break
"""
