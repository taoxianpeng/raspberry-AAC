#!/usr/bin/python3
#-*-coding:utf-8 -*-
import sqlite3
import time
# import random
# import logging
import GetData

class Run():
    def __init__(self,):
        #日志
        #logging.basicConfig(filename='logger.log', level=logging.INFO)
        self.db = sqlite3.connect('./data.db')
        self.cursor = self.db.cursor()
    def run(self,):
        time_set = time.localtime(time.time()) 
        cur_time = '{}-{}-{} {}:{}:{}'.format(
            time_set[0],
            time_set[1],
            time_set[2],
            time_set[3],
            time_set[4],
            time_set[5]
            )
        while True:

            try:
                getdata = GetData.AccData()
                humidity, temperature = getdata.get_wearther_data()
                # humidity, temperature = self.test()
                self.write_data(cur_time,humidity,temperature)

            except Exception as f:
                print(f)

            time.sleep(5)
        self.close()

    def write_data(self, time, humidity, temperature):
        sql_ = 'insert into user values("{}","{}","{}")'.format(time, humidity, temperature)
        print(sql_)
        self.cursor.execute(sql_)
        self.db.commit()
    # def test(self,):
    #     return int(random.random()*100), int(random.random()*100)
    # def get_oneday_data(param='today'):
    #     #获取今天的温度
    #     if param=='today':
    #         datas = self.cursor.execute('select * from DATA;')
    #     dataSet = []
    #     for data in datas；
    #         dataSet.append(data)
    #     return dataSet
    def close(self, ):
        self.cursor.close()

if __name__=='__main__':
    run = Run()
    run.run()