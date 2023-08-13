import json

import uvicorn
from fastapi import FastAPI

import script

app = FastAPI(title="Geo name")


@app.get("/{geonameid}")
def find_city(geonameid: str):
    return script.GetCity.get(geonameid)


@app.get("/pages/")
def find_page_city(page: int, pages: int):
    return script.GetCityPages.get(page, pages)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
