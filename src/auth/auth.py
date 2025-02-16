import requests
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from decouple import config

security = HTTPBearer()


def validate_token(token: str):
    data = {
        "client_id": config("AUTH_CLIENT_ID"),
        "client_secret": config("AUTH_CLIENT_SECRET"),
        "token": token,
    }
    auth_service_url = config("AUTH_BASE_URL")
    response = requests.post(f"{auth_service_url}/token/introspect", data, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    if response.status_code != 200 or not response.json()["active"]:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return response.json()


def auth_request(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    return validate_token(token)