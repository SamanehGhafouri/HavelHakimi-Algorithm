from unittest import TestCase
from havel_hakimi_algorithm import hha
from havel_hakimi_algorithm import find_max_index_in_list
from havel_hakimi_algorithm import find_n_max_index_in_list


class TestBasicHakimi(TestCase):

	def test_in_class_example_one(self):

		expected = {
			'A': ['B', 'C', 'D', 'E'],
			'B': ['A', 'C', 'F', 'G'],
			'C': ['A', 'B', 'D'],
			'D': ['A', 'C'],
			'E': ['A', 'F'],
			'F': ['B', 'E'],
			'G': ['B', 'H'],
			'H': ['G']
		}
		sequence = [4, 4, 3, 2, 2, 2, 2, 1]
		vertices = sorted(expected.keys())

		actual = hha(vertices, sequence)
		self.assertEqual(expected, actual)

	def test_begin_max_value_from_sequence(self):
		sequence = [4, 1, 2, 0]
		expected = (0, 4)
		actual = find_max_index_in_list(sequence)
		self.assertEqual(expected, actual)

	def test_middle_max_value_from_sequence(self):
		sequence = [4, 1, 8, 2, 0]
		expected = (2, 8)
		actual = find_max_index_in_list(sequence)
		self.assertEqual(expected, actual)

	def test_end_max_value_from_sequence(self):
		sequence = [4, 1, 8, 2, 10]
		expected = (4, 10)
		actual = find_max_index_in_list(sequence)
		self.assertEqual(expected, actual)

	def test_3_max_values_from_sequence(self):
		sequence = [0, 3, 2, 1, 1, 2, 2, 1]
		expected = [(1, 3), (2, 2), (5, 2)]
		actual = find_n_max_index_in_list(3, sequence)
		self.assertEqual(expected, actual)

	def test_4_max_values_from_sequence(self):
		sequence = [0, 3, 2, 1, 1, 2, 2, 1]
		expected = [(1, 3), (2, 2), (5, 2), (6, 2)]
		actual = find_n_max_index_in_list(4, sequence)
		self.assertEqual(expected, actual)
