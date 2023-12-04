# Part 1
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

      skip_game = False
      for color, number in t.items():
        if color not in max_cubes:
          print("color not found in game params", color)
          skip_game = True
        if number > max_cubes[color]:
          skip_game = True
      if skip_game:
        add_to_total = False
        break
    if add_to_total:
      total += game_id
      good_games.add(game_id)
  return total

print(sum_of_playable_games("day2file.txt", {"red": 12, "green": 13, "blue": 14}))

# Part 2
def sum_of_all_powers(file):
  # iterate through file and create Games
  with open(file, "r") as file:
    lines = file.readlines()
  
  sum_of_powers = 0
  for line in lines:
    game_info, turns = line.split(":")

    # get game id
    game_id = int(game_info.split()[1])

    min_dict = {"red": 0, "green": 0 ,"blue": 0}
    for turn in turns.split(";"):
      t = {}
      for cubes in turn.split(", "):
        v, k = cubes.split()
        v = int(v)
        t[k] = v
        if k not in min_dict:
          raise ValueError("unknown color not found in dict:", k)
        if v > min_dict[k]:
          min_dict[k] = v

    power = 1
    for v in min_dict.values():
      power *= v
    sum_of_powers += power
  return sum_of_powers

print(sum_of_all_powers("day2file.txt"))