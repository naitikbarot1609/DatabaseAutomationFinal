import mysql.connector
from threading import Thread

# Database connection details
db_config = {
    'host': "automated-mysql-server-group7.mysql.database.azure.com",
    'user': "dbadmin",
    'password': "qwerty@1234",
    'database': "project_db"
}

def run_query(query, params=None):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

# Query functions
def insert_query():
    query = "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES (%s, %s, %s, %s, %s)"
    data = ('Calgary', '2024-12-04', -5.0, 10.0, 76.0)
    run_query(query, data)

def select_query():
    query = "SELECT * FROM ClimateData WHERE temperature > 20"
    run_query(query)

def update_query():
    query = "UPDATE ClimateData SET humidity = 90 WHERE location = 'Toronto'"
    run_query(query)

# Threads for concurrent queries
threads = [
    Thread(target=insert_query),
    Thread(target=select_query),
    Thread(target=update_query)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
