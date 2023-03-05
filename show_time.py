# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 13:21:43 2023

@author: Mokhtar Mahmoudian Mokhy31@gmail.com
"""
import datetime
class Time:
    """showing current time"""
time = Time()
time.H = datetime.datetime.now().strftime("%H")
time.M = datetime.datetime.now().strftime("%M")
time.S = datetime.datetime.now().strftime("%S")
time.p = datetime.datetime.now().strftime("%p")

def printing_time(time):
    print("%s:%s:%s %s"%(time.H,time.M,time.S, time.p))
    
printing_time(time)