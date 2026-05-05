from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

packages = Blueprint("packages", __name__)

@packages.route("/")
def get_packages():
    try:
        conn= get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute("""
                        select * from packages
                       
                """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    
@packages.route("/", methods=["POST"])
def create_packages():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into packages
                    (packages_id, description, weight)
                    values 
                    (%s, %s, %s,)
            """, (data["packages_id"], data["description"] , data["weight"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201
    
@packages.route("/<int:id>", methods=["PUT"])
def update_packages(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update packages
                    set  
                        packages_id = %s,
                       description = %s,
                        weight = %s
                    where packages_id = %s
            """, (data["package_id"], data["description"] , data["weight"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@packages.route("/<int:id>", methods=["DELETE"])
def delete_packages(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from packages
                    where packages_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201
