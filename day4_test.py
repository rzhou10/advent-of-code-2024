from days import day4
import unittest

class TestDays(unittest.TestCase):
    def test_day4_part_one(self):
        # self.assertEqual(day4.part_one("inputs/day4/day4.txt"), 173529487)
        self.assertEqual(day4.part_one("inputs/day4/day4_example.txt"), 18)

    # def test_day4_part_two(self):
        # self.assertEqual(day4.part_two("inputs/day4/day4.txt"), 99532691)
        # self.assertEqual(day4.part_two("inputs/day4/day4_example_part_two.txt"), 48)


if __name__ == '__main__':
    unittest.main()