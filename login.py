import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="mysql",database="shop")
if conn.is_connected():
    print('\t\tConnection Established')
    print('----------------------------------------------------------')
c1 = conn.cursor()
c1.execute('create table login(name varchar(50),user_id varchar(30)primary key,passwd varchar(20))')
