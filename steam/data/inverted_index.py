import json

class InvertedIndex(object):
  def __init__(self):
    self.dicio = {}
    self.id_counter = 0

  def initialize_inverted_index(self, filename):
    """
      Método de InvertedIndex: inicializa um índice invertido 
      baseado em um arquivo

      Param: initialize_inverted_index(filename):
        filename:str - nome do arquivo sobre o qual queremos criar um arquivo
        invertido
    """
    # Dicionário que será o arquivo invertido
    # dicio = {}

    with open(filename) as file:
      file = file.readlines()[1:-1]

      # Inserindo um resgistro do arquivo json no dicionário
      for i,line in enumerate(file):
        if i != len(file)-1:
          line = line[0:-2]

        line = json.loads(line)
        line["id"] = str(self.id_counter)
        self.dicio[str(self.id_counter)] = line
        self.id_counter += 1

    return self.dicio

# Não consegui encaixar essas funções dentro da classe
def update_file(dicionario, filename):
  with open(filename, 'w') as file:
    json.dump(dicionario, file)
  

games = InvertedIndex()
games = games.initialize_inverted_index('games.json')

# Inserindo um item no dicionário
games[10] = {"name":"Teste", "price":"30.00", "publisher":"Nintendo", "id":10}

# Atulizando o arquivo
update_file(games, 'games.json')
