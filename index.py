"""This module contains the actual endpoints by using FastAPI"""

from fastapi import FastAPI
from champions.champion_scraper import get_champ_names, get_champ_stats, get_specific_champ


app = FastAPI()

#returns list of champ names
@app.get("/champions")
async def get_names():
    return get_champ_names()

#returns all champ stats
@app.get("/champions/stats")
async def get_stats():
    return get_champ_stats()

#returns stats for specific champs
@app.get("/champions/{name}/stats")
async def get_specific_stats(name: str):
    return get_specific_champ(name)
