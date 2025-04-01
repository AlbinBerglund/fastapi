import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

PORT = 8031

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

# Sample rooms data
rooms = [
    {
        "id": 1,
        "name": "Living Room",
        "own_by": "alex",
        "size": "25m²"
    },
    {
        "id": 2,
        "name": "Kitchen",
        "own_by": "alexed",
        "size": "15m²"
    },
    {
        "id": 3,
        "name": "Bedroom",
        "own_by": "albert",
        "size": "18m²"
    },
    {
        "id": 4,
        "name": "Bathroom",
        "own_by": "arthur",
        "size": "10m²"
    },
    {
        "id": 5,
        "name": "Dining Room",
        "own_by": "zed",
        "size": "20m²"
    }
]

# Route to return the rooms data
@app.get("/rooms")
def getRooms(request: Request):
    return {"rooms": rooms}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",
        ssl_certfile="/etc/letsencrypt/fullchain.pem",
    )
