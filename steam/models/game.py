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
        splited_name = name.strip().split("+")
        id_set_and = set()
        id_set_or = set()

        # Busca com filtro
        # O sinal '+' indica OR e o ' ' (espaço em branco) indica AND
        # Exemplo: boring paper+potato, retorna todos os jogos que tenham
        # boring paper ou potato no nome
        for word in splited_name:
            inner_words = word.split()
            id_set_and = self._names_table[inner_words[0]]

            for inner_word in inner_words[1:]:
                id_set_and = id_set_and.intersection(self._names_table[inner_word])

            id_set_or = id_set_or.union(id_set_and)
            id_set_and = set()
    
        games_list=[]
        for game_id in id_set_or:
            # Procurados pelos jogos através do ID que está na TRIE
            games_list.append(self.get(game_id))

        by_key = lambda item : item["name"]
        games_list.sort(reverse=order, key=by_key)

        return games_list

    def save_games(self):
        """
        Os jogos que foram adicionados após o setup são salvos
        por essa função.
        """
        with open("archive/dump.json", "w") as write_to:
            json.dump(self._items_list, write_to)

    def update_game(self, changes, key):
        games = self.find_by_name(key)

        # Os únicos atributos que podem ser modificados
        valid_keys = [
            "img_url",
            "name",
            "price",
            "developer",
            "full_desc",
            "publisher",
            "date",
            "popu_tags",
            "url_info",
            "categories"
        ]

        # Podemos atualizar vários jogos de uma só vez ou somente um
        for game in games:
            for k,v in changes.items():
                k = str(k)
                v = str(v)
                if k in valid_keys:
                    game[k] = v

        return games
