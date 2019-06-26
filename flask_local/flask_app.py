from flask import Flask, render_template
from graph import build_graph
import sqlite3
import pandas as pd
from datetime import datetime, date, time, timedelta
 
app = Flask(__name__)
 
@app.route('/graphs')
def graphs():
    now = date.today()
    now_str = now.strftime("%Y-%m-%d")
    yesterday = now-timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    # connect to sqlite database
    conn = sqlite3.connect('../flask_local/temp_bude.db')
    query = "SELECT temp, sqltime FROM sensor_data where sqltime between '{}' and '{}'".format(yesterday_str, now_str)
    # insert into dataframe
    df = pd.read_sql_query(query,conn)
    #define colums
    df.columns = ['temp', 'sqltime']
    #set column sqltime to panda datetimeformat
    df['sqltime'] = pd.to_datetime(df['sqltime'], format="%Y-%m-%d %H:%M:%S")
    # create indexed panda
    indexed_df = df.set_index('sqltime')
    ts = indexed_df['temp']
    graph1_url = build_graph(ts)
    return render_template('graphs.html', graph1=graph1_url, yesterday_str=yesterday_str)


if __name__ == '__main__':
    app.debug = True
    app.run()