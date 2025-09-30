from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow frontend (http://localhost:5173) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only; tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_PASSWORD = "letmein"  # change this to whatever you want

@app.post("/api/login")
def login(password: str = Form(...)):
    if password == SECRET_PASSWORD:
        return {"success": True}
    return {"success": False, "error": "Invalid password"}
