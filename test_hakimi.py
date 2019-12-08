from unittest import TestCase
from havel_hakimi_algorithm import hha
from havel_hakimi_algorithm import find_max_index_in_list
from havel_hakimi_algorithm import find_n_max_index_in_list


# test the code
class TestBasicHakimi(TestCase):

	def test_graphic_in_class_example_one(self):

		# adjacency list that we expect
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

		# returning the keys and sort them
		vertices = sorted(expected.keys())

		actual, _ = hha(vertices, sequence)

		# check if the expected is equal to actual
		self.assertEqual(expected, actual)

	def test_graphic_in_class_example_one(self):

		# adjacency list that we expect
		expected = True
		sequence = [4, 4, 3, 2, 2, 2, 2, 1]

		# returning the keys and sort them
		vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

		_, actual = hha(vertices, sequence)

		# check if the expected is equal to actual
		self.assertEqual(expected, actual)

	def test_non_graphic_sequence_one(self):

		expected = False
		sequence = [4, 3, 3, 2, 2, 2, 2, 1]

		vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

		_, actual = hha(vertices, sequence)

		self.assertEqual(expected, actual)

	def test_non_graphic_sequence_two(self):

		expected = False
		sequence = [4, 4, 3, 3, 2, 2, 2, 2, 1]

		vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

		_, actual = hha(vertices, sequence)

		self.assertEqual(expected, actual)

	# test to find the max value function
	def test_begin_max_value_from_sequence(self):
		sequence = [4, 1, 2, 0]
		expected = (0, 4)
		actual = find_max_index_in_list(sequence)
		self.assertEqual(expected, actual)

	# test if the max value in the middle for the same function finding the max
	def test_middle_max_value_from_sequence(self):
		sequence = [4, 1, 8, 2, 0]
		expected = (2, 8)
		actual = find_max_index_in_list(sequence)
		self.assertEqual(expected, actual)

	# test if the max is at the end
	def test_end_max_value_from_sequence(self):
		sequence = [4, 1, 8, 2, 10]
		expected = (4, 10)
		actual = find_max_index_in_list(sequence)
		self.assertEqual(expected, actual)

	# test for finding the nth max in the list(3 biggest)
	def test_3_max_values_from_sequence(self):
		sequence = [0, 3, 2, 1, 1, 2, 2, 1]
		expected = [(1, 3), (2, 2), (5, 2)]
		actual = find_n_max_index_in_list(3, sequence)
		self.assertEqual(expected, actual)

	# test for finding the nth max( 4 biggest)
	def test_4_max_values_from_sequence(self):
		sequence = [0, 3, 2, 1, 1, 2, 2, 1]
		expected = [(1, 3), (2, 2), (5, 2), (6, 2)]
		actual = find_n_max_index_in_list(4, sequence)
		self.assertEqual(expected, actual)
