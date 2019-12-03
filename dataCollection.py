# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:26:49 2019

@author: Abhi
"""

import os
import time
import requests
import sys

def retrive_pages(year_start, year_end, city_code):
    for year in range(year_start, year_end+1):
        for month in range(1, 13):
            if(month < 10):
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-{}.html'.format(month, year, city_code)
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-{}.html'.format(month, year, city_code)
                
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')
            
            if not os.path.exists("Data/html_Data/{}".format(year)):
                os.makedirs('Data/html_Data/{}'.format(year))
            with open('Data/html_Data/{}/{}.html'.format(year, month), 'wb') as output:
                output.write(text_utf)
                
    sys.stdout.flush()
            
if __name__ == '__main__':
    start_time = time.time()
    retrive_pages(2013, 2019, 426470)
    #city_code 426470 is depicting Ahmedabad India 
    stop_time = time.time()
    print("time taken = {}".format(stop_time-start_time))
    