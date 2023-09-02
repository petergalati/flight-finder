from fastapi import FastAPI, Form
from typing import Annotated
import httpx

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/trip-data/amadeus/get-token")
async def get_amadeus_token(
    grant_type: Annotated[str, Form()],
    client_id: Annotated[str, Form()],
    client_secret: Annotated[str, Form()]
    ):

    url = "https://test.api.amadeus.com/v1/security/oauth2/token"

    form_data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(url, form_data)

    if r.status_code == httpx.codes.OK:
        return {"message": "POST successful", "data": r.access_token}
    else:
        return {"message": f"POST failed with code{r.status_code}"}

