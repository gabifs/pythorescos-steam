from models.entity import Entity

if __name__ == "__main__":
    Test = Entity()

    test1 = {
        "name":"test1",
        "status":"aprovado",
        "price":20.00
    }

    test2 = {
        "name":"test1",
        "status":"reprovado",
        "price":15.00
    }

    Test.create(test1)
    Test.create(test2)

    print(Test._items_list)

    Test.sort_by("price")
    print(Test._items_list)

    print(Test.paginate(1,1))
    print(Test.paginate(2,1))
