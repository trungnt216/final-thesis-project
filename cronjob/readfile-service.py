import json
import sqlite3
import time
import schedule
DB_NAME = "power_data.db"
TABLE_NAME = "power_records"

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  AIRMS REAL NULL,
  AVA REAL NULL,
  AVAR REAL NULL,
  AVRMS REAL NULL,
  AWATT REAL NULL,
  AWATTHR_HI REAL NULL,
  BIRMS REAL NULL,
  BVA REAL NULL,
  BVAR REAL NULL,
  BVRMS REAL NULL,
  BWATT REAL NULL,
  BWATTHR_HI REAL NULL,
  CIRMS REAL NULL,
  CVA REAL NULL,
  CVAR REAL NULL,
  CVRMS REAL NULL,
  CWATT REAL NULL,
  CWATTHR_HI REAL NULL,
  created_at BIGINT NULL
);
"""

def insert_data(data):

  try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(CREATE_TABLE_QUERY)

    data_string = json.dumps(data)

    cursor.execute(f"INSERT INTO {TABLE_NAME} (data) VALUES (?)", (data_string,))
    conn.commit()

    print("Data inserted successfully!")

  except sqlite3.Error as e:
    print("Error inserting data:", e)
  finally:
    if conn:
      conn.close()
def job () : 
   with open("../output.json", "r") as f:
      data = json.load(f)
      print(data)
   # insert_data(data["data"])
def main():
  schedule.every(1).second.do(job)
  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()
