from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from services.articles_service import get_all_articles
from services.orders_service import get_all_orders

load_dotenv()

FRONTEND_URL= os.getenv("FRONTEND_URL")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Webshop API works!"}

@app.get("/api/products")
async def fetch_articles():
    return get_all_articles()

@app.get("/api/orders")
async def fetch_orders():
    return get_all_orders()


