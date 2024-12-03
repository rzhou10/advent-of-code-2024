from days import day2
import unittest

class TestDays(unittest.TestCase):
    def test_day1_part_one(self):
        self.assertEqual(day2.partOne("inputs/day2/day2.txt"), 213)
        self.assertEqual(day2.partOne("inputs/day2/day2_example.txt"), 2)

    def test_day1_part_two(self):
        self.assertEqual(day2.partTwo("inputs/day2/day2.txt"), 4)
        # self.assertEqual(day2.partTwo("inputs/day2/day2_example.txt"), 4)


if __name__ == '__main__':
    unittest.main()