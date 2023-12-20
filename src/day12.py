from copy import deepcopy
import re

def is_valid_arrangement(str, counts):
  pound_groups = re.finditer(r'#+', str)
  for group in pound_groups:
    start_i, end_i = group.span()
    if len(counts) == 0:
      # if you've found extra #s, return false
      return False
    if end_i - start_i != counts.pop(0):
      # if number of #s doesn't match count size, return false
      return False
  # if no more #s are found to be matched, check if counts is empty
  return len(counts) == 0
  

def recursive_check(current_str, pattern_to_match, num_matches):
  q_mark_index = current_str.find('?')
  if q_mark_index == -1:
    # if no more question marks, check validity
    if is_valid_arrangement(current_str, deepcopy(pattern_to_match)):
      return 1
    else:
      return 0
  # try to substitute a '.' and a '#'
  return recursive_check(current_str.replace('?', '.', 1), pattern_to_match, num_matches) + \
      recursive_check(current_str.replace('?', '#', 1), pattern_to_match, num_matches)

if __name__ == '__main__':
  total_matches = 0
  with open("files/day12file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
      result = line.split(' ')
      str, counts = result[0], result[1].split(',')
      int_counts = [int(x) for x in counts]
      total_matches += recursive_check(str, int_counts, 0)
  print("total matches", total_matches)

