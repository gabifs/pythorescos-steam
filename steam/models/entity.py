from steam.data.trie import Trie

class Entity:
    def __init__(self):
        self._counter = 0
        self._items_list = []
        self._items_table = Trie()

    def create(self, item):
        self._counter += 1
        item["id"] = str(self._counter)

        # Alguns atributos não estão preenchidos ou seu valor é do tipo incorreto
        item["name"] = str(item["name"]) if item.get("name") != None else "No name"
        item["date"] = str(item["date"]) if item.get("date") != None else "No date"
        item["publisher"] = str(item["publisher"]) if item.get("publisher") != None else "No publisher"
        item["developer"] = str(item["developer"]) if item.get("developer") != None else "No developer"
        item["price"] = str(item["price"]) if item.get("price") != None else "No price"

        self._items_list.append(item)

        self._items_table[item["id"]] = item
        return item

    def get(self, item_id):
        return self._items_table[item_id]

    def sort_by(self, key):
        by_key = lambda item : item[key]
        return self._items_list.sort(key=by_key)

    def paginate(self, page=1, offset=25):
        return self._items_list[(page-1)*offset:(page)*offset]

