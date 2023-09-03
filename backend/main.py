from fastapi import FastAPI, Form
from typing import Annotated
from datetime import date
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
        r = await client.post(url, data = form_data)

    if r.status_code == httpx.codes.OK:
        data = r.json()
        return {"message": "POST successful", "data": data.get("access_token")}
    else:
        return {"message": f"POST failed with code {r.status_code}"}
    
@app.get("/trip-data/amadeus/flights/inspiration")
async def get_flight_inspo(
    origin: str,
    destination: str,
):
    API_KEY = "do7rWOFZ04PGHmc0nc7h3X1wLST0L6tc"
    API_SECRET = "Wo1S8xK2rMfmU8WJ"
    BASE_URL = "https://test.api.amadeus.com/v1"

    api_token = await get_amadeus_token("client_credentials", API_KEY, API_SECRET)

    # not sure yet
    endpoint = "/shopping/flight-dates"

    # not sure yet
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    parameters = {
        "origin" : origin,
        "destination" : destination,
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url = BASE_URL + endpoint, headers = headers, params = parameters)

        if r.status_code == httpx.codes.OK:
                results = r.json()
                return results
        else:
            return {"message": f"API GET request failed with code {r.status_code}"}


