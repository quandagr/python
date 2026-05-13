from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

Vehicle = Blueprint("Vehicle", __name__)

@Vehicle.route("/")
def get_Vehicle():
    try:
        conn= get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute(
            'select * from "vehicle"'
            )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    
@Vehicle.route("/", methods=["POST"])
def create_Vehicle():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into vehicle
                    (vehicle_id, license_plate,model )
                    values 
                    (%s, %s, %s)
            """, (data["vehicle_id"],data["license_plate"], data["model"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201
    
@Vehicle.route("/<int:id>", methods=["PUT"])
def update_vehicle(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update vehicle
                    set 
                        vehicle_id = %s,
                        license_plate = %s,
                        model = %s
                    where vehicle_id = %s
            """, (data["vehicle_id"],data["license_plate"], data["model"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@Vehicle.route("/<int:id>", methods=["DELETE"])
def delete_Vehicle(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from vehicle
                    where vehicle_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201