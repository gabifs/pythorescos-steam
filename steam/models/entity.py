from steam.data.trie import Trie

class Entity:
    def __init__(self):
        self._counter = 0
        self._items_list = []
        self._items_table = Trie()

    def create(self, item):
        self._counter += 1

        if item.get("id") == None:
            item["id"] = str(self._counter)

        # Alguns atributos não estão preenchidos ou seu valor é do tipo incorreto
        item["name"] = str(item["name"]) if item.get("name") != None else "No name"
        item["date"] = str(item["date"]) if item.get("date") != None else "No date"
        item["publisher"] = str(item["publisher"]) if item.get("publisher") != None else "No publisher"
        item["developer"] = str(item["developer"]) if item.get("developer") != None else "No developer"
        item["price"] = str(item["price"]).strip("0") if item.get("price") != None else "No price"
        
        item["img_url"] = str(item["img_url"]) if item.get("img_url") != None else "No url"
        item["full_desc"] = str(item["full_desc"]) if item.get("full_desc") != None else "No description"
        item["popu_tags"] = str(item["popu_tags"]) if item.get("popu_tags") != None else "No tags"
        item["url_info"] = str(item["url_info"]) if item.get("url_info") != None else "No url infos"
        item["categories"] = str(item["categories"]) if item.get("categories") != None else "No categories"
        

        self._items_list.append(item)

        self._items_table[item["id"]] = item
        return item

    def get(self, item_id):
        return self._items_table[item_id]

    def sort_by(self, key, order=False):
        by_key = lambda item : item[key]
        return self._items_list.sort(reverse=order, key=by_key)

    def paginate(self, page=1, offset=25):
        return self._items_list[(page-1)*offset:(page)*offset]

