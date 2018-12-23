from util.DBLink import *
import random
handler = easy_connect()
s = handler.SELECT("select * from student")
for i in s:
    stu_id = i[0]
    major_id = int(random.random() * 13) + 1
    while(major_id==7):
        major_id = int(random.random() * 13) + 1
    handler.UPDATE("insert into major_student values(%s,%s)",(stu_id,major_id))
