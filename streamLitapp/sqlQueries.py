import mysql.connector
import pandas as pd

# Function to fetch data from MySQL
def fetch_data_from_mysql(query):
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Dev@n$h!@28",
        database="redbus"
    )
    #query = "SELECT * FROM bus_routes"
    data = pd.read_sql(query, db)
    db.close()
    return data

# def fetch_locations():  
#     db = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="Dev@n$h!@28",
#         database="redbus"
#     )
#     query1 = "SELECT Routes FROM route_name"
#     Routes =pd.read_sql(query1,db)
#     db.close()
#     return Routes