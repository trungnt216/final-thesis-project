import json
import os
import psycopg2
import schedule
import time
from dotenv import load_dotenv
load_dotenv()

DB_NAME =  os.getenv('DB_DATABASE')
TABLE_NAME = os.getenv('TABLE_NAME')
PG_USER = os.getenv('DB_USERNAME')
PG_PASSWORD = os.getenv('DB_PASSWORD')
PG_HOST = os.getenv('DB_HOST')
PG_PORT = os.getenv('DB_PORT')

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS test_table (
  id SERIAL PRIMARY KEY,
  data JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def init_table(cursor):
    cursor.execute(CREATE_TABLE_QUERY)


def insert_data(cursor, data):
    try:
        # conn = psycopg2.connect(
        #     dbname=DB_NAME,
        #     user=PG_USER,
        #     password=PG_PASSWORD,
        #     host=PG_HOST,
        #     port=PG_PORT
        # )
        # cursor = conn.cursor()

        cursor.execute(CREATE_TABLE_QUERY)
        print(data)

       # cursor.execute("INSERT INTO {TABLE_NAME} (data) VALUES (%s)", (json.dumps(data),))
        #conn.commit()

        print("Data inserted successfully!")

    except psycopg2.Error as e:
        print("Error inserting data:", e)
    # finally:
    #     if conn:
    #         conn.close()

def job(cursor):
    for filename in os.listdir("../data"):
        if filename.startswith("metter_output_"):
            file_path = os.path.join("../data", filename)
            with open(file_path, "r") as f:
                data = json.load(f)
                insert_data(cursor,data["data"])
                # os.remove(file_path)
            new_file_path = os.path.join("../processed_data", filename)
            os.rename(file_path, new_file_path) 

def main():
    try:
        
        print("Beginning program...")
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=PG_USER,
            password=PG_PASSWORD,
            host=PG_HOST,
            port=PG_PORT
        )
        cursor = conn.cursor()

        init_table(cursor)

        schedule.every(1).minutes.do(job, cursor)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()