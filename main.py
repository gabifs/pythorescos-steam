from utils.startup import setup

Games_model, Tags_model, Categories_model, Enterprises_model = setup()

if __name__ == "__main__":
  # game = {
  #   "name":"Boring paper",
  #   "price":"free",
  #   "developer":"Valve",
  #   "publisher":"Valve",
  #   "date":"19 May, 2021"}
  # Games_model.create(game)
  # games = Games_model.find_by_name("boring paper+potato")

  Games_model.sort_by("name")
  games = Games_model.paginate()

  for game in games:
    print(game["name"])

  # Games_model.save_new_games()
  
  # Games_model.sort_by("name")
  # games = Games_model.paginate(1,80893)

  # for game in games:
  #   print(game["name"])
