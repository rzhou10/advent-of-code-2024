from days import day3
import unittest

class TestDays(unittest.TestCase):
    def test_day3_part_one(self):
        self.assertEqual(day3.partOne("inputs/day3/day3.txt"), 173529487)
        self.assertEqual(day3.partOne("inputs/day3/day3_example.txt"), 161)

    def test_day3_part_two(self):
        self.assertEqual(day3.partTwo("inputs/day3/day3.txt"), 99532691)
        self.assertEqual(day3.partTwo("inputs/day3/day3_example_part_two.txt"), 48)


if __name__ == '__main__':
    unittest.main()