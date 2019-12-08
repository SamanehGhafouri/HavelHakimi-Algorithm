from typing import List, Dict, Tuple


# find the max value in the list for giving a list of numbers return index and number
def find_max_index_in_list(sequence: List[int]) -> (int, int):

	max_index = 0
	max_value = sequence[0]
	for current_index in range(1, len(sequence)):
		current_value = sequence[current_index]
		if current_value > max_value:
			max_index = current_index
			max_value = current_value

	return max_index, max_value


def find_n_max_index_in_list(n: int, sequence: List[int]) -> List[Tuple[int, int]]:
	# we want to modify the sequence so we make a copy
	c_sequence = sequence.copy()

	result: List[(int, int)] = []
	while n > 0:
		n -= 1
		index, value = find_max_index_in_list(c_sequence)
		result.append((index, value))

		# index + 1 will include the index itself
		for pre_index in range(0, index + 1):
			# we already found it so it is equal to 0
			c_sequence[pre_index] = 0

	return result


# An arrow -> indicates a return type will follow
def hha(vertices: List[str], sequence: List[int]) -> Tuple[Dict[str, List[str]], bool]:

	is_graphic = True
	adjacency_list: Dict[str, List[str]] = {}
	# initialize the adjacency list with empty list of neighbours
	for vertex_key in vertices:
		adjacency_list[vertex_key] = []

	print("It's Havel Time!!!")

	while True:
		# finding the max number
		m_index, m_value = find_max_index_in_list(sequence)
		# if the largest value we found is 0 we stop
		if m_value == 0:
			# stopping condition
			break
		# update the sequence the max is now 0
		sequence[m_index] = 0
		list_of_max = find_n_max_index_in_list(m_value, sequence)
		for pair in list_of_max:
			# pair[index, value] only care about the index
			target_index = pair[0]
			# decrement the max numbers
			sequence[target_index] -= 1

			# print(f"Vertex Pairs({vertices[m_index]}, {vertices[target_index]})")
			neighbours = adjacency_list[vertices[m_index]]
			# add a neighbour to the vertex at index m
			neighbours.append(vertices[target_index])

			neighbours = adjacency_list[vertices[target_index]]
			neighbours.append(vertices[m_index])

	return adjacency_list, is_graphic