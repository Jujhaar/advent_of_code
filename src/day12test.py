import unittest

from day12 import is_valid_arrangement


class TestDay12(unittest.TestCase):
  def test_valid_cases(self):
    self.assertEqual(is_valid_arrangement("#.#.###", [1,1,3]), True)
    self.assertEqual(is_valid_arrangement(".#...#....###", [1,1,3]), True)
    self.assertEqual(is_valid_arrangement("#.#.###", [1,1,3]), True)
    self.assertEqual(is_valid_arrangement(".#...#....###.", [1,1,3]), True)
    self.assertEqual(is_valid_arrangement(".#.###.#.######", [1,3,1,6]), True)
    self.assertEqual(is_valid_arrangement("####.#...#...", [4,1,1]), True)
    self.assertEqual(is_valid_arrangement("#....######..#####.", [1,6,5]), True)
    self.assertEqual(is_valid_arrangement(".###.##....# ", [3,2,1]), True)
  
  def test_invalid_wrong_number(self):
    self.assertEqual(is_valid_arrangement("#.#.###", [1,2,3]), False)

  def test_invalid_list_too_short(self):
     self.assertEqual(is_valid_arrangement("#.#.#", [1,1]), False)

  def test_invalid_list_too_long(self):
     self.assertEqual(is_valid_arrangement("#.#.#", [1,1,1,1]), False)


if __name__ == '__main__':
    unittest.main()