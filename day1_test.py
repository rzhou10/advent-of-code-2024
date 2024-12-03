from days import day1
import unittest

class TestDays(unittest.TestCase):
    def test_day1_part_one(self):
        self.assertEqual(sum(day1.partOne("inputs/day1/day1.txt")), 1941353)
        self.assertEqual(sum(day1.partOne("inputs/day1/day1_example.txt")), 11)

    def test_day1_part_two(self):
        self.assertEqual(sum(day1.partTwo("inputs/day1/day1.txt")), 22539317)
        self.assertEqual(sum(day1.partTwo("inputs/day1/day1_example.txt")), 31)


if __name__ == '__main__':
    unittest.main()