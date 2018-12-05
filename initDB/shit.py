from public.DBLink import *
import random

BOY = []
GIRL = []
seek = 0
result = []
f = open('initDB/name','r')
for line in f.readlines():
    temp = line.strip()
    if temp!="":
        if temp=="男":
            seek=1
        elif temp=="女":
            seek=2
        else:
            if seek==1:
                BOY.append((temp,'男'))
            else:
                GIRL.append((temp,'女'))
result=BOY+GIRL
random.shuffle(result)

sql = "insert into student values(%s,%s,%s,%s,%s,%s)"
id_pre= [11410000,11510000,11310000]
id_dict = {11410000:0,11510000:0,11310000:0}
new_result = []
for temp in result:
    sex = temp[1]
    name = temp[0]
    id_key = random.choice(id_pre)
    id_dict[id_key]+=1
    id = id_key+id_dict[id_key]
    if str(id)[2]==4:
        year = 2014
    elif str(id)[2]==5:
        year = 2015
    else:
        year = 2013
    graduate= year+4
    new_result.append((id,name,year,graduate,sex,'待业'))
new_result = sorted(new_result,key=lambda temp:temp[0])

server = SQLServer()
handler = SQLHandler(server.getConn())
for temp in new_result:
    handler.UPDATE(sql,temp)