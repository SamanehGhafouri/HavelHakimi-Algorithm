from typing import List, Dict, Tuple, Optional

__character_map = {
	1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M",
	14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y",
	26: "Z"
}


def is_sum_of_sequence_odd(sequence: List[int]) -> bool:
	if sum(sequence) % 2 != 0:
		return True
	return False


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

		c_sequence[index] = 0

	return result


def vertex_character_map(key: int) -> str:
	return __character_map[key]


# An arrow -> indicates a return type will follow! returning an adjecency list and info if its graphic or not
def hha(vertices: Optional[List[str]], sequence: List[int]) -> Tuple[Dict[str, List[str]], bool]:
	# auto labeling of nodes
	if vertices is None or len(vertices) < len(sequence):
		vertices = []
		for index in range(len(sequence)):
			character = vertex_character_map(index + 1)
			vertices.append(character)

	# initialization
	is_graphic = True
	adjacency_list: Dict[str, List[str]] = {}
	# initialize the adjacency list with empty list of neighbours
	for vertex_key in vertices:
		adjacency_list[vertex_key] = []

	# basic hakimi check
	if is_sum_of_sequence_odd(sequence):
		is_graphic = False
		return adjacency_list, is_graphic

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

			# building the adjacency list of numbers
			neighbours = adjacency_list[vertices[m_index]]
			neighbours.append(vertices[target_index])  # add a neighbour to the vertex at index m

			neighbours = adjacency_list[vertices[target_index]]
			neighbours.append(vertices[m_index])

	return adjacency_list, is_graphic
