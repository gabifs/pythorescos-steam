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

    def delete_game(self, key):
        """
        Podemos deletor vários jogos de uma vez ou um único jogo
        """
        games = self.find_by_name(key, from_deletion=True)

        # O resto dos dados é mantido em memória, até que os dados sejam salvos
        for game in games:
            # for word in game["name"].strip().split():
            #     word = word.lower()

                # Deletando a referência do ID no _names_table
                # self._names_table[word].remove(game["id"])

            # Deletando a referência do ID da TRIE
            self._items_table.erase(game)

            # Deletando o elemento do array _items_list, que usamos para salvar
            # os dados no arquivo
            self._items_list.remove(game)

    def find_by_name(self, name, order=False, from_deletion=False):
        """
        name (string): nome do jogo que será buscado
        order (boolean): False (default) - ordem crescente, True - ordem descrescente
        from_deletion (boolean): False (default) - find_by_name foi chamada por 
            delete_game, então não exiba os nomes dos jogos buscados, 
            True - find_by_name não foi chamada por delete_game, então exiba
            os nomes dos jogos buscados
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

            # Após a deleção, alguns palavras foram excluídas
            # isso geraria um Key Error
            i = 0
            for inner_word in inner_words:
                i += 1
                if inner_word in self._names_table:
                    id_set_and = self._names_table[inner_word]
                    break

            for inner_word in inner_words[i:]:
                id_set_and = id_set_and.intersection(self._names_table[inner_word])

            id_set_or = id_set_or.union(id_set_and)
            id_set_and = set()
    
        games_list=[]
        # Procurados pelos jogos através do ID que está na TRIE
        for game_id in id_set_or:
            game_id = self.get(game_id)
            if game_id != None:
                games_list.append(game_id)

        # Se a lista estiver vazia, pode ocorrer por conta da deleção
        if len(games_list) == 0:
            print("Nenhum jogo foi encontrado.")
            return []

        # Ordenando o resultado da busca por nome
        by_key = lambda item : item["name"]
        games_list.sort(reverse=order, key=by_key)

        # Se a função delete_game chamou a função find_by_name, não queremos
        # exibir o nome dos jogos
        if not from_deletion:
            for game in games_list:
                print(game["name"])

        return games_list

    def save_games(self):
        """
        Os jogos que foram adicionados após o setup são salvos
        por essa função. 

        Mesmo que os jogos sejam criados, atualizados ou deletados, se 
        os dados não forem salvos, todas as modificações serão perdidas.
        """
        with open("archive/steam_data.json", "w") as write_to:
            json.dump(self._items_list, write_to)
