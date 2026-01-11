from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from dotenv import load_dotenv
import os

from auth.auth import authenticate_user, create_access_token
from auth.middleware import require_admin
from shemas.shemas import LoginData

load_dotenv()

FRONTEND_URL = os.getenv("FRONTEND_URL", "").strip()

origins = []
if FRONTEND_URL:
    origins.append(FRONTEND_URL)

origins += ["http://localhost:5174", "http://localhost:3000", "http://localhost:3001"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login")
async def login(data: LoginData):
    user = authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# test ruta da vidiš da admin guard radi
@app.get("/admin/ping")
async def admin_ping(_payload=Depends(require_admin)):
    return {"ok": True}
