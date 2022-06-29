from flask import Flask
import controlador
import psycopg2
from flask_wtf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

conn = psycopg2.connect(
        host="localhost",
        database="ginyu",
        user="Grove",
        password="root")
cur = conn.cursor()

@app.route("/<query>")
def main(query):
    print(query)
    return controlador.main(query, cur)

app.run(port=5002, debug=True)