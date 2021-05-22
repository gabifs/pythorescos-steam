#
# Henrique Peixoto & Gabriel Fernandes
#

# Se quiser restaurar os dados de steam vá para a função save_game no arquivo
# game.py

from steam.models.game import Game
from utils.startup import setup

# Inicializando a aplicação com a função setup
Games_model, Tags_model, Categories_model, Enterprises_model = setup()

if __name__ == "__main__":
  # Seguem alguns exemplos de algumas operações que podem ser feitas
  
  # Inserção de dados
  game = {
    "name": "Boring paper",
    "price": "free",
    "developer": "Valve",
    "publisher": "Valve",
    "date": "19 May, 2021"
  }
  Games_model.create(game)

  # Vamos procurar o jogo que acabamos de criar 
  print("Procurando 'Boring paper'")
  Games_model.find_by_name("boring paper", show_all_info=True)

  # Vamos atualizar o preço e a publisher do jogo que
  # acabamos de criar
  changes = {"price":"499","publisher":"Sony"}
  Games_model.update_game(changes, "boring paper")

  # Vamos exibir o resultado desse mudança, pesquisando
  # novamente pelo jogo "Boring paper"
  print()
  Games_model.find_by_name("boring paper", show_all_info=True)

  # Vamos deletar o jogo "Boring paper"
  Games_model.delete_game("boring paper")

  # Vamos buscar pelo jogo "Boring paper" após a sua deleção
  print("Procurando por 'Boring paper'")
  Games_model.find_by_name("boring paper")

  # Vamos ordenar os dados
  print()
  print("Ordenando os dados")
  print()

  print("Ordenandod em ordem crescente")
  Games_model.sort_by("developer")
  games_sorted = Games_model.paginate(1,50)

  for game in games_sorted:
    print(game["developer"], game["name"])

  print()

  print("Ordenando em ordem decrescente")
  Games_model.sort_by("publisher", True)
  games_sorted = Games_model.paginate(1,50)

  for game in games_sorted:
    print(game["publisher"], game["name"])

  # Vamos realizar algumas buscas usando os filtros AND e OR
  print()
  print("Filtro AND")
  Games_model.find_by_name("call duty")
  print()

  print()
  print("Filtro OR")
  Games_model.find_by_name("potato+paper")
  print()

  print()
  print("Filtro OR e AND")
  Games_model.find_by_name("call duty+potato")
  print()

  # Vamos deletar todos os jogos que tenham a palavra "potato"
  # nome
  Games_model.delete_game("potato")

  # Em seguida vamos salvar todas as alterações
  print()
  print("Salvando dados")
  Games_model.save_games()




  # Segundo exemplo
  # Comente o exemplo anterior para que ele não seja executado novamente
  # No último exemplo, deletamos todos os jogos com a palavra
  # "potato" no nome, após isso, salvamos os dados. Portanto,
  # se procurar por "potato" não encontraremos nada, vamos ver se funciona.

  # print("Procurando por 'potato' após a deleção e salvamento dos dados")
  # Games_model.find_by_name("potato")