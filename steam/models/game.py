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
        """
        Atualiza os dados de um jogo.

        changes (dicionário): dicionário com as mudanças que devem ser aplicadas
        key (string): nome do jogo que deve ter seus dados alterados
        """
        print("Atualizando jogos, por favor, aguarde.")
        games = self.find_by_name(key, called_by_user=False)

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

        updated_games = []

        # Podemos atualizar vários jogos de uma só vez ou somente um
        for game in games:
            index = self._items_list.index(game)
            name_before = game["name"].lower()

            # Mudando os dados do jogo
            for k,v in changes.items():
                k = str(k).lower()
                v = str(v)
                if k in valid_keys:
                    game[k] = v

            name_after = game["name"].lower()


            # Atualizando as informações do jogo na TRIE
            self._items_table[game["id"]] = game

            # O _imtens_list é o array que será salvo no arquivo, por isso
            # precisamos atualizar seus dados quando atualizamos um jogo
            self._items_list[index] = game

            # Também precisamos atualizar os conjuntos de nomes
            if name_before != name_after:
                name_before = name_before.lower().split()
                name_after = name_after.lower().split()

                name_before_set = set()
                name_after_set = set()
                for name in name_before: name_before_set.add(str(name))
                for name in name_after: name_after_set.add(str(name))

                # Precisamos adicionar os ID nos conjuntos para as novas palavras que
                # estão no nome do jogo
                new_names = set()
                new_names = name_after_set.difference(name_before_set)

                # É necessário verificar se a palavra que vamos inserir já existe ou não
                for name in new_names:
                    if name not in self._names_table:
                        self._names_table[name] = {game["id"]}
                    else:
                        self._names_table[name].add(game["id"])

                # Precisamos retirar os ID dos conjuntos após mudar o nome do jogo
                old_names = set()
                old_names = name_before_set.difference(name_after_set)

                for name in old_names:
                    self._names_table[name].remove(game["id"])

            updated_games.append(game)

        print("Jogos atualizados.")
        return updated_games

    def delete_game(self, key):
        """
        Podemos deletor vários jogos de uma vez ou um único jogo.

        key (string): nome do jogo que será deletado.
        """
        print("Deletando jogos, por favor, aguarde.")
        games = self.find_by_name(key, called_by_user=False)

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

        print("Jogos deletados.")

    def find_by_name(self, name, order=False, called_by_user=True):
        """
        name (string): nome do jogo que será buscado
        order (boolean): False (default) - ordem crescente, True - ordem descrescente
        called_by_user (boolean): True (default) - find_by_name foi chamada pelo
            pelo usuário, então exiba os nomes dos jogos buscados, 
            False - find_by_name foi chamada por delete_game ou update_game, 
            então não exiba os nomes dos jogos buscados
        """
        if called_by_user:
            print("Buscando jogos, por favor aguarde.")

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
            # se pesquisássemos por elas, isso geraria um Key Error
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

        # Se a função delete_game ou update_game chamou a função find_by_name, 
        # não queremos exibir o nome dos jogos buscados
        if called_by_user:
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
        print("Salvando os dados, por favor, aguarde.")
        with open("archive/steam_data.json", "w") as write_to:
            json.dump(self._items_list, write_to)
        print("Dados salvos.")
