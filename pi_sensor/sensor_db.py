#!/usr/bin/python
import Adafruit_DHT as A
from datetime import datetime
import sqlite3
from sqlite3 import Error

#sensor = A.DHT22
#pin = 4

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_data(conn, data):
    sql = ''' INSERT INTO sensor_data(temp, humidity) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid

def main():
    database = "/home/pi/temp.db"
    sensor = A.DHT22
    pin = 4
    hum, temp = A.read_retry(sensor, pin)
    conn = create_connection(database)

    with conn:
        #data = (int(temp), int(hum))
        data = (temp, hum)
        create_data(conn, data)

if __name__ == '__main__':
    main()
        


#now = datetime.now()

#hum, temp = A.read_retry(sensor, pin)




#print('{0};{1:0.1f};{2:0.1f}'.format(now, temp, hum))
