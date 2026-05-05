from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
from database import get_connection, init_db
from routes.driver import Driver
from routes.packages import packages
from routes.routes import Routes
from routes.vehicle import Vehicle

init_db()

app = Flask(__name__)
app.register_blueprint(Driver, url_prefix="/driver")
app.register_blueprint(packages, url_prefix="/packages")
app.register_blueprint(Routes, url_prefix="/routes")
app.register_blueprint(Vehicle, url_prefix="/vehicle")


@app.route("/")
def home():
    return jsonify({"message": "Server Online"})


if __name__ == "__main__":
    app.run(debug=True)