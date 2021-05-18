from steam.models.game import Game
from steam.models.entity import Entity
import json
import datetime
import re

def date_parser(date:str):
    months = {
        "jan":1,"feb":2,"mar":3,"apr":4,
        "may":5,"jun":6,"jul":7,"aug":8,
        "sep":9,"oct":10,"nov":11,"dec":12
    }
    month, day, year= date.split()
    year = int(year)
    month = months[month.lower()]
    day = int(day.replace(",",''))
    return datetime.datetime(year, month, day)

def dict_to_game(d):
    g_raw = {
                    "name": d["name"]
            }
    if "full_desc" in d:
        g_raw["description"] = d["full_desc"]["desc"]
    else:
        g_raw["description"] = "Sem descrição"

    if "price" in d and re.search("^\d+", d["price"]):
        g_raw["price"] = float(d["price"])
    else:
        g_raw["price"] = "free"

    if "data" in d:
        g_raw["date"] = date_parser(d["date"])
    else:
        g_raw["date"] = datetime.datetime.now()

    return g_raw



def setup():
    Games_model = Game()
    Tags_model = Entity()
    Categories_model = Entity()
    Enterprises_model = Entity()

    """
    Inicializa estruturas
    """

    with open("archive/steam_data.json") as file_content:
        games_raw = json.loads(file_content.read())
        for dict_raw in games_raw:
            game_raw = dict_to_game(dict_raw)

        game = Games_model.create(game_raw)

    return (Games_model, Tags_model, Categories_model, Enterprises_model)
