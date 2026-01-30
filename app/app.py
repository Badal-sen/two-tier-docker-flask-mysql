from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "rootpass")
DB_NAME = os.getenv("DB_NAME", "mydb")

def get_conn():
    # MySQL takes a few seconds to start, so retry
    for _ in range(25):
        try:
            return mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
        except:
            time.sleep(1)
    raise Exception("MySQL not ready")

@app.route("/")
def home():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT 'Two-tier OK: Flask -> MySQL (Docker network)'")
    msg = cur.fetchone()[0]
    cur.close()
    conn.close()
    return msg

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

