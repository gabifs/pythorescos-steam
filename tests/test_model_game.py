from steam.models.game import Game

def test_new_game():
    Games = Game()
    assert Games._counter == 0
    assert len(Games._items_list) == 0
    assert Games._items_table is not None
    assert Games._names_table is not None

def test_create():
    Games = Game()
    g = {
        "name":"Dorime ameno",
        "price": 15,
        "description": "Lorem ipsum dolorem",
        "date": "24 Nov 2015"
    }

    g = Games.create(g)
    assert len(Games._items_list) == 1
    assert g["id"] == "1"

def test_find_by_name():
    Games = Game()
    g1 = {
        "name":"Dorime ameno",
        "price": 15,
        "description": "Lorem ipsum dolorem",
        "date": "24 Nov 2015"
    }

    g2 = g1.copy()
    g2["name"] = "Dorime latire"

    Games.create(g1)
    Games.create(g2)

    assert len(Games.find_by_name("Dorime")) == 2
    assert Games.find_by_name("latire")[0] == g2
