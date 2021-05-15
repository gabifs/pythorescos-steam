from models.game import Game
from models.entity import Entity


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
        "name":"dorime ameno",
        "price":16
    }

    g = Games.create(g)

    #laço for
    t = Tags.create(t)

    #laço for
    c = Categories.create(c)

    #laço for
    e = Enterprises.create(e)


    print(Games.get((g["id"])))
    print(t)
    print(c)
    print(e)


    # print(Games._items_list)
    # print(Games._names_table)

    # Games.sort_by("price")
    # print(Games._items_list)

