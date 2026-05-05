from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

Routes = Blueprint("Routes", __name__)

@Routes.route("/")
def get_appointments():
    try:
        conn= get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute("""
                        select * from Routes 
                       
                """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    
@Routes.route("/", methods=["POST"])
def create_routes():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into routes
                    ( routes_id, date, service_zone)
                    values 
                    (%s, %s, %s,)
            """, (data["routes_id"], data["date"] , data["service_zone"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201
    
@Routes.route("/<int:id>", methods=["PUT"])
def update_routes(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update routes
                    set  
                        routes_id = %s,
                       date = %s,
                        service_zone = %s
                    where routes_id = %s
            """, (data["route_id"],data["date"], data["service_zone"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@Routes.route("/<int:id>", methods=["DELETE"])
def delete_routes(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from routes
                    where routes_id= %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201