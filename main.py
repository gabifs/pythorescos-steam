from steam.models.game import Game
from utils.startup import setup

Games_model, Tags_model, Categories_model, Enterprises_model = setup()

if __name__ == "__main__":

  # game = {
  #   "name":"Boring paper",
  #   "price":"free",
  #   "developer":"Valve",
  #   "publisher":"Valve",
  #   "date":"19 May, 2021"
  # }

  # Games_model.create(game)

  # changes = {"price":"499","publisher":"Sony"}
  # Games_model.update_game(changes, "boring paper")

  Games_model.delete_game("simulator+potato")

  # Games_model.find_by_name("simulator")

  # games = Games_model.find_by_name("simulator+potato+paper")
  # for game in games:
  #   print(game["name"])

  # Games_model.save_games()
  # boring_paper = Games_model.find_by_name("boring paper")

  # O jogo antes das mudanças
  # print(boring_paper)

  # Vamos procurar o jogo excluído
  # Games_model.delete_game("boring paper")
  # boring_paper = Games_model.find_by_name("boring paper")

  # print(boring_paper)

  # # O jogo depois das mudanças
  # print(boring_paper)


  # changes = {"name":"Am I a joke to you?"}
  # games = Games_model.update_game(changes, "simulator")

  # for game in games:
  #   print(game["name"])
  

  # print(boring_paper)



  # games = Games_model.find_by_name("boring paper+potato")

  # Games_model.sort_by("name")
  # games = Games_model.paginate()

  # for game in games:
  #   print(game["name"])

  # Games_model.save_games()
  
  # Games_model.sort_by("name")
  # games = Games_model.paginate(1,80893)

  # for game in games:
  #   print(game["name"])
