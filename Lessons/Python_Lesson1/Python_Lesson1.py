
import psycopg2 as pg
#import psycopg2.errors
from psycopg2.errors import *

'''
host: 192.168.1.22:5432  === localhost:5432
user: postgres
pass: admin
DB name: ???
'''

dbName   = 'test_db'
dbCreate = f'CREATE DATABASE {dbName};'
# I

# conn = pg.connect( host='localhost', port='5432',
#                    user='postgres', password='admin' )
# conn.autocommit = True
# cur = conn.cursor()
# cur.execute( dbCreate )
# conn.commit()
# conn.close()

# II
dbHost = "localhost"
dbPort = 5432
conn = pg.connect( f'dbname={dbName} host={dbHost} port={dbPort} '+
                   f'user=postgres password=admin' )
conn.autocommit = True
# Работа с БД "DataBase_231"
createTable1 = """
DROP TABLE IF EXISTS table1;
CREATE TABLE IF NOT EXISTS table1
(
    id BIGSERIAL PRIMARY KEY,
    name varchar(100) UNIQUE NOT NULL,
    birth_day DATE NOT NULL,
    group_ varchar(20) DEFAULT('SEP-231'),
    mark FLOAT  DEFAULT(1) CHECK(mark>0.0) NOT NULL
)
"""
cur = conn.cursor()
try:
    cur.execute(createTable1)
except Error as er:
    print('Error: ',er)

sqlInsert1 = """
INSERT INTO table1(name,birth_day, group_, mark) VALUES
('Temirlan', '1999-11-30', 'SDP-221', 12)
"""
sqlInsert2 = """
INSERT INTO table1(name,birth_day, group_, mark) VALUES
('Shadow', '1999-11-30', 'SKYRIM', 10.5)
"""

try:
    cur.execute(sqlInsert1)
    cur.execute(sqlInsert2)
except Error as er:
    print('Error: ', er)

sqlSelect1 = "SELECT * FROM table1;"
sqlSelect2 = """
SELECT id, name, mark 
FROM table1 
WHERE id = 1
"""

try:
    #cur.execute(sqlSelect1)
    #cur.execute(sqlSelect2, (2))
    cur.execute(sqlSelect2)
    for col in cur.description:
        print(col[0], end='\t')
    print()
    for row in cur.fetchall():
        print(row)
except Error as er:
    print('Error: ', er)

conn.close()
print('Done')