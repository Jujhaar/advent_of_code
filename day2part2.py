from functools import reduce
import re

def sum_of_all_powers(file):
  # iterate through file and create Games
  with open(file, "r") as file:
    lines = file.readlines()
  
  sum_of_powers = 0
  for line in lines:
    game_info, turns = line.split(":")

    # get game id
    game_id = int(game_info.split()[1])

    max_dict = {"red": 0, "green": 0 ,"blue": 0}
    for turn in turns.split(";"):
      t = {}
      for cubes in turn.split(", "):
        v, k = cubes.split()
        v = int(v)
        t[k] = v
        if k not in max_dict:
          raise ValueError("unknown color not found in dict:", k)
        if v > max_dict[k]:
          max_dict[k] = v

    power = 1
    for v in max_dict.values():
      power *= v
    print("max values for game", game_id, max_dict, int(power))
    sum_of_powers += power
  return sum_of_powers

print(sum_of_all_powers("day2file.txt"))