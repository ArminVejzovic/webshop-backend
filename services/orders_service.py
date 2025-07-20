import requests
import os
from dotenv import load_dotenv

load_dotenv()

ORDERS_API_URL= os.getenv("ORDERS_API_URL")

def get_all_orders():
    response = requests.get(ORDERS_API_URL)
    return response.json()
