# from public.DBLink import SQLServer
# #
# # x = pymssql.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,database=DB_NAME,charset="utf8")
# # cur = x.cursor()
# #cur.execute("insert into test values(1)")
# # cur.execute("select * from test",())
# # c = cur.fetchall()
#
# x=SQLServer()
# c = x.SELECT("select * from test",())
# # c = x.UPDATE("insert into test values(%s)",(1))
# print(c)

a = {}
a['233'] = "2333"
print(a)