from models.entity import Entity

class Game(Entity):
    def __init__(self):
        super().__init__()
        self._names_table = {}


    def create(self, item):
        item = super().create(item)

        for word in item["name"].strip().split():
            word = word.lower()
            if word not in self._names_table:
                # cria conjunto (set) de itemns
                self._names_table[word] = {item["id"]}
            else:
                # add o item em conjunto exitente
                self._names_table[word].add(item["id"])
        return item

    def find_by_name(self, name):
        splited_name = name.strip().split()
        games_set = set()
        for word in splited_name:
            games_set.union(self._names_table[word])

        return list(games_set)

