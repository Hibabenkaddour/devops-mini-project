import os
from flask import Flask
import psycopg2

app = Flask(__name__)

def db_is_ok():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            dbname=os.getenv("DB_NAME", "postgres"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres"),
            port=int(os.getenv("DB_PORT", "5432")),
        )
        conn.close()
        return True
    except Exception:
        return False

@app.route("/")
def home():
    status = "✅ DB Connected" if db_is_ok() else "❌ DB Not Connected"
    return f"Hello DevOps World! <br><br>Database status: {status}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
