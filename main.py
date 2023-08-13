import uvicorn
from fastapi import FastAPI

import script

app = FastAPI(title="Geo name")


@app.get("/{geonameid}")
def read_root(geonameid: str):
    return script.get(geonameid)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
