from utils.startup import setup

Games_model, Tags_model, Categories_model, Enterprises_model = setup()

if __name__ == "__main__":
  game = {"name":"Boring paper"}
  Games_model.create(game)
  simulators = Games_model.find_by_name("boring+paper+potato", True)

  for game in simulators:
    print(game["name"])

  # Games_model.save_new_games()
  
  # Games_model.sort_by("name")
  # games = Games_model.paginate(1,80893)

  # for game in games:
  #   print(game["name"])
