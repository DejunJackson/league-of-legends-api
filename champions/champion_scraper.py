"""This module is the actual scraper and returns the results based on which method is required"""
import requests
from bs4 import BeautifulSoup
from champions.util import get_champ_dict
from config import champs_URL


response = requests.get(champs_URL)

page = response.text

champ_soup = BeautifulSoup(page, "html.parser")


def get_champ_names():
    champ_scraper = [name.getText() for name in champ_soup.select(
        "tbody > tr > td > span > span[style*='white-space:normal'] > a")]
    champ_names = {}
    champ_names['champ_names'] = champ_scraper
    return champ_names


def get_champ_stats():
    champs = get_champ_dict()

    # returns a dictionary of each champs stats in puts them in a list
    champ_stats = [champs[champ].serialize() for champ in champs]
    return champ_stats


def get_specific_champ(name: str):
    champs = get_champ_dict()
    cap_name = name.capitalize()

    try:
        return champs[cap_name].serialize()
    except:
        return "Champ not found. This search is not cap sensitive so please check spelling. "
