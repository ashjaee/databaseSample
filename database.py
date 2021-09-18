import psycopg2
try:
    conn = psycopg2.connect(
        host = '127.0.0.1', #or 'localhost'
        user = 'postgres',
        password = '2727',
        database = 'ashjaeiDb')
    print("Connection to database succeeded...")
except:
    print("Connection to database failed...")        
    conn.close()

print('-----------------------------------')

try:
   with conn.cursor() as cursor:
       #insert
       query1 = """insert into person values ('sara','asadi',1016,100)"""
       #cursor.execute(query1)
       #conn.commit()
       #select
       query2 = "SELECT * FROM PERSON where serial > 1007 "
       cursor.execute(query2)
       result = cursor.fetchall()   #or fetchone()
       print(result) #OOOORRRR
       for rec in result:
            print('serial {} name is   : '.format(rec[2]),rec[0])
            print('serial {} famili is : '.format(rec[2]),rec[1])
            print('serial {} age is    : '.format(rec[2]),rec[3])
            print('-------------------------')
       #delete
       #query3 = """delete from person where age = 72"""
       #cursor.execute(query3)
       #conn.commit()
       #update
       #query3 = """update person set age = 900 where age = 80"""
       #cursor.execute(query3)
       #conn.commit()
       #
       #print(result)
       print('-----------------------------------')
       
finally:
    conn.close()
    print("Connection to database closed...")

