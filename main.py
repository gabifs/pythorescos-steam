from steam.models.game import Game
from steam.models.entity import Entity
import json

if __name__ == "__main__":
    Games = Game()
    Tags = Entity()
    Categories = Entity()
    Enterprises = Entity()

    t = {
        "name": "bla"
    }

    c = {
        "name": "blabla"
    }

    e = {
        "name": "blablabla"
    }

    g = {
        "name":"dorime ameno simulator",
        "price":16
    }

    h = {
        "name":"War simulator",
        "price":10
    }

    """
    Teste com o arquivo
    """
    file_content = open("archive/steam_data.json")
    file = file_content.read()
    file = json.loads(file)
    file_content.close()
    
    for game in file:
        game = Games.create(game)

    # g = Games.create(g)
    # h = Games.create(h)

    # #laço for
    # t = Tags.create(t)

    # #laço for
    # c = Categories.create(c)

    # #laço for
    # e = Enterprises.create(e)

    # Abrindo o arquivo

    # print(Games.get(g["id"]))
    # print(Games.get(h["id"]))
    # print(t)
    # print(c)
    # print(e)

    # print(Games._items_list)
    # print(Games._names_table)

    # Ordenando por nome
    Games.sort_by("date")
    games_sorted = Games.paginate(1,80893)
    
    for game in games_sorted:
        print(game["name"], game["date"])
