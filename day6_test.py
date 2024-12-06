from days import day6
import unittest

class TestDays(unittest.TestCase):
    def test_day6_part_one(self):
        self.assertEqual(day6.part_one("inputs/day6/day6.txt"), 173529487)
        self.assertEqual(day6.part_one("inputs/day6/day6_example.txt"), 41)

    # def test_day6_part_two(self):
    #     self.assertEqual(day6.part_two("inputs/day6/day6.txt"), 99532691)
    #     self.assertEqual(day6.part_two("inputs/day6/day6_example_part_two.txt"), 48)


if __name__ == '__main__':
    unittest.main()