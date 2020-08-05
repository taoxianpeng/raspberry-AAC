#!/usr/bin/python3
#-*-coding:utf-8 -*-
import sqlite3
import time
import logging
import GetData

class Run():
    def __init__(self,):
        #日志
        logging.basicConfig(filename='logger.log', level=logging.INFO)
        db = sqlite3.connect('./data.db')
        cursor = db.cursor()
    def run():
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
            time.sleep(2)
            try:

                humidity, temperature = GetData.get_wearther_data()
                self.write_data(cur_time,humidity,temperature)

            except Exception as f:
                logging.WARNING(f)

    def write_data(time, humidity, temperature):
        self.cursor.execute('insert into DATA values({},{},{});'.format(time, humidity, temperature))
    # def get_oneday_data(param='today'):
    #     #获取今天的温度
    #     if param=='today':
    #         datas = self.cursor.execute('select * from DATA;')
    #     dataSet = []
    #     for data in datas；
    #         dataSet.append(data)
    #     return dataSet
    def close():
        self.cursor.close()

if __name__=='__main__':
    run = Run()
    run.run()