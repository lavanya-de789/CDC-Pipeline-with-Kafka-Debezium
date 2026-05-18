import psycopg2
import time

conn=psycopg2.connect(
host='localhost',
database='inventory',
user='postgres',
password='postgres'
)

cursor=conn.cursor()

rows=[
(1,'John','Dallas'),
(2,'Edward','Austin'),
(3,'Sarah','Houston')
]

for row in rows:

    cursor.execute(
    '''
    insert into customers
    values(%s,%s,%s)
    ''',row)

    conn.commit()

    print('inserted:',row)

    time.sleep(5)
