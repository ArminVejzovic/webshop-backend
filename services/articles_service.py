import requests
import os
from dotenv import load_dotenv

load_dotenv()

ARTICLES_API_URL = os.getenv("ARTICLES_API_URL")

def get_all_articles():
    response = requests.get(ARTICLES_API_URL)
    return response.json()
