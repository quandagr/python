import psycopg2 
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection ():
    conn = psycopg2.connect(
      host = os.getenv("DB_HOST"),
      port = os.getenv("DB_PORT"),
      dbname = os.getenv("DB_NAME"),
      user = os.getenv("DB_USER"),
      password = os.getenv("DB_PASSWORD"),
      sslmode = os.getenv("DB_SSLMODE", "require")
    )
    
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    sql="""
                
        CREATE TABLE IF NOT EXISTS Driver (
            driver_id SERIAL PRIMARY KEY,
            name VARCHAR(250) UNIQUE NOT NULL,
            license VARCHAR(50) NOT NULL
           
        );
        CREATE TABLE IF NOT EXISTS Vehicle (
            vehicle_id SERIAL PRIMARY KEY,
            license_plate VARCHAR(50) UNIQUE NOT NULL,
            model VARCHAR(50) NOT NULL
           
        );    
         CREATE TABLE IF NOT EXISTS packages (
            packages_id SERIAL PRIMARY KEY,
            description VARCHAR(250) UNIQUE NOT NULL,
           weight numeric NOT NULL
        
        );  
         CREATE TABLE IF NOT EXISTS Routes (
            routes_id SERIAL PRIMARY KEY,
           date date UNIQUE NOT NULL,
           service_zone VARCHAR(250) NOT NULL
           
        ); 
                  
     """
    cur.execute(sql.strip())
    conn.commit()
    cur.close()
    conn.close()
    print("Database initialized successfully.")

    
