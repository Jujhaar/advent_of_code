import re

def create_char_matrix(filename):
  char_matrix = []
  with open(filename, "r") as file:
    lines = file.readlines()
    for line in lines:
      char_line = [c for c in line]
      char_matrix.append(char_line)
  return char_matrix

def is_valid_symbol(char_matrix, x, y):
  return x >= 0 and y >= 0 and \
    x < len(char_matrix) and y < len(char_matrix[0]) and \
    char_matrix[x][y] not in ('.','0','1','2','3','4','5','6','7','8','9', '\n')

def adjacent_coordinates_has_symbol(char_matrix, i, startj, endj):
  for x in range(i-1, i+2):
    for y in range(startj-1, endj+2):
      if is_valid_symbol(char_matrix, x, y):
        return True
  return False

def engine_schematic_part_numbers_sum(filename, char_matrix):
  num_sum = 0
  with open(filename, "r") as file:
    lines = file.readlines()
    valid_nums = []
    invalid_nums = []

    for i, line in enumerate(lines):
      nums = re.findall('\d+', line)

      # check if they have a symbol near them
      j = 0
      for num in nums:
        match = re.search(num, line[j:])
        startj = j + match.span()[0]
        endj = j + match.span()[1]-1
        if adjacent_coordinates_has_symbol(char_matrix, i, startj, endj):
          num_sum += int(num)
          valid_nums.append(num)
        else:
          invalid_nums.append(num)
        j = endj+1
    print(valid_nums, '\n', invalid_nums, '\n', num_sum)
    return num_sum


char_matrix = create_char_matrix("files/day3file.txt")
print(engine_schematic_part_numbers_sum("files/day3file.txt", char_matrix))
