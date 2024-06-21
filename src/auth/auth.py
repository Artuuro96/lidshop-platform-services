import requests
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from decouple import config
import jwt

security = HTTPBearer()


def validate_token(token: str):
    auth_service_url = config("ACMA_URL")
    response = requests.post(auth_service_url + "/auth/verify", json={}, headers={
        "Authorization": "Bearer " + token
    })
    user = jwt.decode(token, options={"verify_signature": False})

    if response.status_code != 201:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user


def auth_request(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    return validate_token(token)