from public.DBLink import *
import random
handler = easy_connect()
info = handler.SELECT("select * from student")
majors = handler.SELECT("select * from major")
ids = []
majorids = []
for temp in info:
    ids.append(temp[0])
for temp in majors:
    majorids.append(temp[0])

sql = "insert into major_student values(%s,%s)"
for id in ids:
    majorid = random.choice(majorids)
    handler.UPDATE(sql,(id,majorid))
