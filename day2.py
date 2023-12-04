import re
class CubeSet:
  def __init__(self, r_cubes, b_cubes, g_cubes):
    self.r = r_cubes
    self.b = b_cubes
    self.g = g_cubes

class Game:
  def __init__(self, id, cube_sets:[CubeSet]):
    self.id = id
    self.cube_sets = cube_sets

def sum_of_playable_games(file, max_cubes):
  # iterate through file and create Games
  with open(file):
    lines = file.readlines()
  for line in lines:
    game_info, turns = str.split(":")
    # get game id
    game_id = re.findall('\d', game_info)[0]
    print(game_id)
    # get array of cube sets
  # sum ids of games that are legit
  

cases = [
    CubeSet(10,5,3),
    CubeSet(15, 6, 6),
    CubeSet(8, 12, 20),
    CubeSet(3, 19, 18)
  ]
max_c = CubeSet(14, 18, 20)


def is_game_possible(cubes_subset:CubeSet, max_cubes:CubeSet):
  return cubes_subset.r <= max_cubes.r and \
    cubes_subset.b <= max_cubes.b and \
    cubes_subset.g <= max_cubes.g

for cubes in cases:
 # for id, cubes in case:
  print(cubes, max_c, is_game_possible(cubes, max_c))
