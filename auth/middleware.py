from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

from auth.auth import decode_token, is_admin_payload

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def require_admin(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not is_admin_payload(payload):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return payload
