import json

class InvertedIndex(object):
  def __init__(self):
    self._inverted_index = {}
    self._id_counter = 0
    self._stop_words = []
    self._load_stop_words()

  def initialize_inverted_index(self, filename, create_using):
    """
      - Método de InvertedIndex: inicializa um índice invertido 
      baseado em um arquivo
      - Param: initialize_inverted_index(filename):
        * filename:str - nome do arquivo sobre o qual queremos criar um arquivo
        invertido
        * create_using:str - campo que será utilzado para criar o arquivo invertido
    """
    # Abrindo o arquivo e fazendo o parsing do json
    x = open(filename).read()
    file = json.loads(x)

    # Criando o arquivo invertido baseado no nome do jogo
    for i, game in enumerate(file):
      key_selected = str(game[create_using]).strip().replace(":","").lower().split(" ")

      # Criamos uma entrada no inverted index para cada palavra no nome do jogo
      for word in key_selected:
        # Se essa palavra não for uma stop word
        if word not in self._stop_words:
          # Se o dicionário do jogo não tem o campo 'id', então adicionamos
          if file[i].get("id") == None:
            file[i]["id"] = self._id_counter
            self._id_counter += 1

          # Se o array associado a uma palavra não existe, temos que inicializá-lo
          if self._inverted_index.get(word) == None:
            self._inverted_index[word] = []

          self._inverted_index[word].append(file[i]["id"])
        
    return self._inverted_index

  def _load_stop_words(self):  
    """
      - Método de InvertedIndex: carrega em um array as stop words
      - Param: _load_stop_words():
        * Nenhum parâmetro
    """
    with open('stop_words.txt') as file:
      for line in file.readlines():
        line = line.strip()
        self._stop_words.append(line)

# Não consegui encaixar essas funções dentro da classe
def update_file(dicionario, filename):
  array = []

  for item in dicionario:
    array.append(item)

  with open(filename, 'w') as file:
    json.dump(array, file)

def print_inverted_index(dicionario):
  for i, item in dicionario.items():
    print(i, item)

if __name__ == "__main__":
  games = InvertedIndex()
  # Adicione o arquivo
  # games = games.initialize_inverted_index('final_data_new.json','name')

  print_inverted_index(games)

  # Descomente para escrever o arquivo invertido no games.txt
  # file = open('games.txt','a')
  # for game, id in games.items():
  #   string = game + " " + str(id) + "\n"
  #   file.write(string)
  # file.close()q


  # Atulizando o arquivo
  # update_file(games, 'games.json')
