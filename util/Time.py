# coding=utf-8
import time

# 输出本地时间 从年到秒 举例 "2018-07-20 20:00:00"
def from_year_to_second():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 输出本地时间 从年到秒 举例 "2018-07-20_20:00:00"
def from_year_to_second_secure():
    return time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())

# 输出本地时间 从年到分 举例 "2018-07-20 20:00"
def from_year_to_minute():
    return time.strftime("%Y-%m-%d %H:%M", time.localtime())

def get_year():
    return time.strftime("%Y",time.localtime())

# 将天转换成秒
def change_day_to_second(day):
    seconds = float(day * 24 * 60 * 60)
    return seconds

# 输出本地时间 从年到天 举例 "2018-07-20"
def from_year_to_day():
    return time.strftime("%Y-%m-%d", time.localtime())

# 获取现在的本地时间
def get_unix_time():
    return time.time()

def get_unix_time_by_format(it_time):
    good_time = time.strptime(it_time,"%Y-%m-%d %H:%M:%S")
    return time.mktime(good_time)




