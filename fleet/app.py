from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from database import get_connection, init_db
from routes.driver import Driver
from routes.packages import packages
from routes.routes import Routes
from routes.vehicle import Vehicle

init_db()

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# ── API Blueprints ────────────────────────────────────────────────────────────
app.register_blueprint(Driver,   url_prefix="/driver")
app.register_blueprint(packages, url_prefix="/packages")
app.register_blueprint(Routes,   url_prefix="/routes")
app.register_blueprint(Vehicle,  url_prefix="/vehicle")

# ── Health check ─────────────────────────────────────────────────────────────
@app.route("/api/health")
def health():
    return jsonify({"message": "Server Online"})

# ── Static assets produced by Vite ───────────────────────────────────────────
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('static/assets', filename)

@app.route('/favicon.svg')
def favicon():
    return send_from_directory('static', 'favicon.svg')

@app.route('/icons.svg')
def icons():
    return send_from_directory('static', 'icons.svg')

# ── Catch-all: hand every other route to React Router ────────────────────────
# Must be LAST so the API blueprints above take priority
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
