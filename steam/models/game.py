from steam.models.entity import Entity

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
        id_set = set()
        for word in splited_name:
            word = word.lower()
            id_set = id_set.union(self._names_table[word])

        games_list=[]
        for game_id in id_set:
            games_list.append(self.get(game_id))
        return games_list



