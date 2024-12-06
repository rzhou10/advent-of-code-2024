from days import day5
import unittest

class TestDays(unittest.TestCase):
    def test_day5_part_one(self):
        self.assertEqual(day5.part_one("inputs/day5/day5_ordering.txt", "inputs/day5/day5_updates.txt"), 6505)
        self.assertEqual(day5.part_one("inputs/day5/day5_example_pages_ordering.txt", "inputs/day5/day5_example_pages_updates.txt"), 143)

    # def test_day5_part_two(self):
        # self.assertEqual(day5.part_two("inputs/day5/day5.txt"), 99532691)
        # self.assertEqual(day5.part_two("inputs/day5/day5_example_part_two.txt"), 48)


if __name__ == '__main__':
    unittest.main()