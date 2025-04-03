import os, uvicorn, psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

PORT = 8031

#load enviroment variables
load_dotenv()
DB_URL = os.getenv("DB_URL")

#create dp connection
conn = psycopg.connect(DB_URL, autocommit=True, row_factory=dict_row)
# Create the FastAPI app
app = FastAPI()

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Route to return the rooms data
@app.get("/rooms")
def get_rooms():
    with conn.cursor() as cur:
        cur.execute("SELECT *  FROM hotel_rooms")
        messages = cur.fetchall()
        return messages

@app.get("/rooms/{id}")
def get_rooms_id(id: int):
    try:
        return {"msg: " "hello"}
    except: 
        return {"error:" "Room no found"}
    
@app.post("/bookings")
def create_booking(request: Request):
    return {"msg:" "booking created!"}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",
        ssl_certfile="/etc/letsencrypt/fullchain.pem",
    )
