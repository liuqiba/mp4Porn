from scrapy.cmdline import execute  
execute(['scrapy', 'crawl', 'sihu']);  
# -*- coding: utf-8 -*-

"""
import pymongo
import sys
import traceback    

MONGODB_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
    'db_name': 'xyd',
    'username': None,
    'password': None
}

class MongoConn(object):

    def __init__(self):
        # connect db
        try:
            self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            self.db = self.conn[MONGODB_CONFIG['db_name']]  # connect db
            self.username=MONGODB_CONFIG['username']
            self.password=MONGODB_CONFIG['password']           
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except Exception:
            print( traceback.format_exc())
            print ('Connect Statics Database Fail.')
            sys.exit(1)   



# -*- coding: utf-8 -*-

if __name__ == "__main__":
    my_conn = MongoConn()
    datas = [
        {'_id':1, 'data':12},        
        {'_id':2, 'data':22},
        {'_id':3, 'data':'cc'}      
    ]  
    #插入数据，'mytest'是上文中创建的表名
    my_conn.db['mytest'].insert(datas)
    #查询数据，'mytest'是上文中创建的表名
    res=my_conn.db['mytest'].find({})
    for k in res:
        print (k)
"""