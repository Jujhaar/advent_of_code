import re

def sum_of_playable_games(file, max_cubes):
  total = 0
  good_games = set()

  # iterate through file and create Games
  with open(file, "r") as file:
    lines = file.readlines()
  for line in lines:
    game_info, turns = line.split(":")

    # get game id
    game_id = int(game_info.split()[1])

    # get array of cube sets
    add_to_total = True
    for turn in turns.split(";"):
      t = {}
      for cubes in turn.split(", "):
        v, k = cubes.split()
        t[k] = int(v)
      print(t)

      skip_game = False
      for color, number in t.items():
        if color not in max_cubes:
          print("color not found in game params", color)
          skip_game = True
        if number > max_cubes[color]:
          print("too many cubes in this turn", number, max_cubes[color], color)
          skip_game = True
      if skip_game:
        add_to_total = False
        break
    if add_to_total:
      total += game_id
      good_games.add(game_id)
      print(total, "added to total", game_id)
      print(good_games)
  return total

print(sum_of_playable_games("day2file.txt", {"red": 12, "green": 13, "blue": 14}))