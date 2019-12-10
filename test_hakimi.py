from unittest import TestCase
from havel_hakimi_algorithm import hha
from havel_hakimi_algorithm import find_max_index_in_list
from havel_hakimi_algorithm import find_n_max_index_in_list
from havel_hakimi_algorithm import is_sum_of_sequence_odd

from typing import List


# test the code
class TestBasicHakimi(TestCase):

	# Test Helper
	def is_sequence_sum_for_task_four_odd(self, sequence: List[int]) -> bool:
		return is_sum_of_sequence_odd(sequence)

	# Test Helper
	def sequence_for_task_four(self, n: int, i: int):

		result = []
		for val in range(1, n):
			result.append(val)
			if i == val:
				result.append(val)

		result.reverse()
		return result

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

	def test_graphic_sequence_two(self):

		# adjacency list that we expect
		expected = True
		sequence = [4, 3, 2, 2, 1]

		# returning the keys and sort them
		vertices = ['A', 'B', 'C', 'D', 'E']

		_, actual = hha(vertices, sequence)

		# check if the expected is equal to actual
		self.assertEqual(expected, actual)

	def test_graphic_sequence_3(self):

		# adjacency list that we expect
		expected = True
		sequence = [3, 3, 3, 3, 3, 3, 2, 2]

		# returning the keys and sort them
		vertices = ['A', 'B', 'C', 'D', 'E']

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

	def test_non_graphic_sequence_3(self):

		expected = False
		sequence = [4, 4, 3, 2]

		vertices = ['A', 'B', 'C', 'D']

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

	def test_2_max_values_from_sequence_out_of_order(self):
		sequence = [0, 0, 1, 1, 1, 1, 0, 2, 1]
		expected = [(7, 2), (2, 1)]
		actual = find_n_max_index_in_list(2, sequence)
		self.assertEqual(expected, actual)

	def test_sum_of_sequence_is_odd(self):
		sequence = [4, 4, 3, 2]
		expected = True
		actual = is_sum_of_sequence_odd(sequence)
		self.assertEqual(expected, actual)

	def test_sum_of_sequence_is_even(self):
		sequence = [3, 3, 3, 3, 3, 3, 2, 2]
		expected = False
		actual = is_sum_of_sequence_odd(sequence)
		self.assertEqual(expected, actual)

	# The first Task to test
	def test_barnoy_req_2_by_n(self):

		n_sequence = [6, 7, 8, 9, 10, 11, 12]
		for n in n_sequence:
			sequence = [2] * n
			expected = True
			_, actual = hha(None, sequence)
			with self.subTest():

				# check if the expected is equal to actual
				self.assertEqual(expected, actual)

	# The second task test
	def test_barnoy_req_3_by_n(self):

		n_sequence = [4, 6, 8, 10, 12, 14, 16]
		for n in n_sequence:
			sequence = [3] * n
			expected = True
			_, actual = hha(None, sequence)
			with self.subTest():

				# check if the expected is equal to actual
				self.assertEqual(expected, actual)

	# The third task test
	def test_barnoy_req_k_by_n(self):

		k_sequence = [1, 2, 3, 4, 5, 6]
		n_sequence = [2, 4, 6, 8, 10, 12]
		for index in range(0, len(k_sequence)):
			sequence = [k_sequence[index]] * n_sequence[index]
			expected = True
			_, actual = hha(None, sequence)
			with self.subTest():
				# check if the expected is equal to actual
				self.assertEqual(expected, actual)

	def test_barnoy_task_four(self):

		n_sequence = [6, 7, 8, 9]
		i_sequence_end = [5, 6, 7, 8]
		for n_index in range(0, len(n_sequence)):
			n = n_sequence[n_index]
			i_sequence = [x for x in range(1, i_sequence_end[n_index] + 1)]
			for i in i_sequence:
				sequence = self.sequence_for_task_four(n, i)
				expected = not self.is_sequence_sum_for_task_four_odd(sequence)
				_, actual = hha(None, sequence)
				with self.subTest():
					# check if the expected is equal to actual
					self.assertEqual(expected, actual)




