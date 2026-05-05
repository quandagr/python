from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

Driver = Blueprint("Driver", __name__)

@Driver.route("/")
def get_driver():
    try:
        conn= get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute (
            'select * from "driver"'
            )
                       
            
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    
@Driver.route("/", methods=["POST"])
def create_driver():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into driver
                    (driver_id, name, license)
                    values 
                    (%s, %s, %s)
            """, (data["driver_id"], data["name"] , data["license"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201
    
@Driver.route("/<int:id>", methods=["PUT"])
def update_driver(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update driver
                    set 
                        driver_id= %s,
                        name = %s,
                       license = %s
                    where driver_id = %s
            """, (data["driver_id"], data["name"] , data["license"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@Driver.route("/<int:id>", methods=["DELETE"])
def delete_driver(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from driver
                    where driver_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201