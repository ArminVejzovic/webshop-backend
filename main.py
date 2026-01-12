from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordRequestForm

from auth.auth import authenticate_user, create_access_token
from auth.middleware import require_admin
from shemas.shemas import LoginData

from retool_proxy import (
    RETOOL_ARTICLES_URL,
    RETOOL_ORDERS_URL,
    retool_get, retool_post, retool_put, retool_delete
)

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

# ---------- PUBLIC (GUEST) ----------
@app.get("/api/articles")
async def get_articles():
    return await retool_get(RETOOL_ARTICLES_URL)

@app.get("/api/articles/{article_id}")
async def get_article(article_id: int):
    return await retool_get(f"{RETOOL_ARTICLES_URL}/{article_id}")

@app.post("/api/orders")
async def create_order(payload: dict):
    """
    Guest kreira narudžbu.
    payload neka bude ono što tvoj frontend već šalje.
    """
    return await retool_post(RETOOL_ORDERS_URL, payload)

# ---------- ADMIN (JWT) ----------
@app.get("/api/admin/articles", dependencies=[Depends(require_admin)])
async def admin_get_articles():
    return await retool_get(RETOOL_ARTICLES_URL)

@app.post("/api/admin/articles", dependencies=[Depends(require_admin)])
async def admin_create_article(payload: dict):
    return await retool_post(RETOOL_ARTICLES_URL, payload)

@app.put("/api/admin/articles/{article_id}", dependencies=[Depends(require_admin)])
async def admin_update_article(article_id: int, payload: dict):
    return await retool_put(f"{RETOOL_ARTICLES_URL}/{article_id}", payload)

@app.delete("/api/admin/articles/{article_id}", dependencies=[Depends(require_admin)])
async def admin_delete_article(article_id: int):
    return await retool_delete(f"{RETOOL_ARTICLES_URL}/{article_id}")

@app.get("/api/admin/orders", dependencies=[Depends(require_admin)])
async def admin_get_orders():
    return await retool_get(RETOOL_ORDERS_URL)

@app.put("/api/admin/orders/{order_id}", dependencies=[Depends(require_admin)])
async def admin_update_order(order_id: int, payload: dict):
    return await retool_put(f"{RETOOL_ORDERS_URL}/{order_id}", payload)