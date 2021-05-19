from os import write
from steam.models.entity import Entity
import json

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
                # add o item em conjunto existente
                self._names_table[word].add(item["id"])
        return item

    def find_by_name(self, name, order=False):
        """
        name (string): nome do jogo que será buscado
        order (boolean): False - ordem crescente, True - ordem descrescente
        """
        splited_name = name.strip().split()
        id_set = set()
        for word in splited_name:
            word = word.lower()
            id_set = id_set.union(self._names_table[word])

        games_list=[]
        for game_id in id_set:
            # Procurados pelos jogos através do ID que está na TRIE
            games_list.append(self.get(game_id))

        by_key = lambda item : item["name"]
        games_list.sort(reverse=order, key=by_key)
        return games_list

    def save_new_games(self):
        """
        Os jogos que foram adicionados após o setup são salvos
        por essa função.
        """
        with open("archive/dump.json", "w") as write_to:
            json.dump(self._items_list, write_to)
