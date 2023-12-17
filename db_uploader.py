
import sys
import pymysql
from dotenv import load_dotenv
import os
import csv 

load_dotenv()


def mysqlDbConnection(u, pw, h, p, d):
    try:
        conn = pymysql.connect(user = u, password = pw, host = h, port = p, database = d)
        print("DB Connection Success: {0}".format(h))
    except pymysql.Error as e:
        print("Error connecting to MySQL Platform : {}".format(e))
        sys.exit(1)
 
    return conn
 
 
def mysqlDbClose(_dbConn):
    try:
        _dbConn.close()
        print("DB Close Success")
    except pymysql.Error as e:
        print("Error closing from MySQL Platform")
        sys.exit(1)


db_username = os.getenv("SECERT_DB_USERNAME")
db_password = os.getenv("SECERT_DB_PASSWORD")
db_port = os.getenv("SECERT_DB_PORT")
db_database = os.getenv("SECERT_DB_DATABASE")
db_host = os.getenv("SECERT_DB_HOST")

file_url = './musinsa_shoes.csv'
clothes_category = 'SHOES'

dbConn = mysqlDbConnection(db_username, db_password, db_host, int(db_port), db_database)
cursor = dbConn.cursor()
 
 
file = open(file_url,'r', encoding='utf-8-sig')
fReader = csv.reader(file)
 
for line in fReader:
    # query = "INSERT INTO clothes VALUES ('{0}', '{1}', '{2}', {3})".format(line[0], line[1], line[2], line[3])
    query = "INSERT INTO clothes(clothes_category, brand, name, image_url, sell_url) VALUES ('{0}' ,'{1}', '{2}', '{3}', '{4}')".format(clothes_category, line[0], line[1], line[2], line[3])
    
    cursor.execute(query)

file.close()

dbConn.commit() 
cursor.close()
mysqlDbClose(dbConn)


