from public.DBLink import easy_connect
print(easy_connect().SELECT("select password from admin where user_name = 'jack'"))