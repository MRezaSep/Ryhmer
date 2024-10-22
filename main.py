# import from packages
import pronouncing
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


# init
app = FastAPI(
    title="Ryhmer",
    description="Find a list of cool ryhmes ;)",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
)


# access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define a Pydantic model for the request body
class RhymeRequest(BaseModel):
    word: str


# send home page to client
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root():
    with open("index.html") as f:
        return f.read()


# ryhmer route
@app.post("/rhyme")
async def get_rhyme(request: RhymeRequest):
    rhymes = pronouncing.rhymes(request.word)
    return {"rhymes": rhymes}
