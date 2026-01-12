import os
import httpx
from fastapi import HTTPException

RETOOL_ARTICLES_URL = os.getenv("RETOOL_ARTICLES_URL")
RETOOL_ORDERS_URL = os.getenv("RETOOL_ORDERS_URL")

if not RETOOL_ARTICLES_URL or not RETOOL_ORDERS_URL:
    raise RuntimeError("Missing RETOOL_ARTICLES_URL / RETOOL_ORDERS_URL in .env")

async def retool_get(url: str):
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url)
    if r.status_code >= 400:
        raise HTTPException(status_code=502, detail=f"Retool GET failed: {r.status_code}")
    return r.json()

async def retool_post(url: str, payload: dict):
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.post(url, json=payload)
    if r.status_code >= 400:
        raise HTTPException(status_code=502, detail=f"Retool POST failed: {r.status_code}, body={r.text[:200]}")
    return r.json()

async def retool_put(url: str, payload: dict):
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.put(url, json=payload)
    if r.status_code >= 400:
        raise HTTPException(status_code=502, detail=f"Retool PUT failed: {r.status_code}, body={r.text[:200]}")
    return r.json()

async def retool_delete(url: str):
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.delete(url)
    if r.status_code >= 400:
        raise HTTPException(status_code=502, detail=f"Retool DELETE failed: {r.status_code}")
    return {"deleted": True}
