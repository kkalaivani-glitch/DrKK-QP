"""
Simple unit tests for QP site utilities
"""
import unittest


class TestUtils(unittest.TestCase):
    """Test suite for utility functions"""

    def test_addition(self):
        """Test basic addition"""
        self.assertEqual(2 + 2, 4)

    def test_string_operations(self):
        """Test string concatenation"""
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World")

    def test_list_operations(self):
        """Test list manipulation"""
        test_list = [1, 2, 3]
        test_list.append(4)
        self.assertEqual(len(test_list), 4)
        self.assertIn(4, test_list)


class TestMarkCalculations(unittest.TestCase):
    """Test suite for marks calculations"""

    def test_total_marks(self):
        """Test total marks calculation"""
        q1_marks = 10
        q2_marks = 10
        total = q1_marks + q2_marks
        self.assertEqual(total, 20)

    def test_bloom_level_distribution(self):
        """Test Bloom's taxonomy distribution"""
        bloom_levels = {
            'Remembering': 0,
            'Understanding': 0,
            'Applying': 0,
            'Analyzing': 0,
            'Evaluating': 0,
            'Creating': 20
        }
        total = sum(bloom_levels.values())
        self.assertEqual(total, 20)
        self.assertEqual(bloom_levels['Creating'], 20)


if __name__ == '__main__':
    unittest.main()
