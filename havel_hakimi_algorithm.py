from typing import List, Dict, Tuple


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

	c_sequence = sequence.copy()

	result: List[(int, int)] = []
	while n > 0:
		n -= 1
		index, value = find_max_index_in_list(c_sequence)
		result.append((index, value))

		for pre_index in range(0, index + 1):
			c_sequence[pre_index] = 0

	return result


# An arrow -> indicates a return type will follow
def hha(vertices: List[str], sequence: List[int]) -> Dict[str, List[str]]:

	result: Dict[str, List[str]] = {}
	for vertex_key in vertices:
		result[vertex_key] = []

	print("It's Havel Time!!!")

	while True:
		m_index, m_value = find_max_index_in_list(sequence)
		if m_value == 0:
			# stopping condition
			break
		sequence[m_index] = 0
		list_of_max = find_n_max_index_in_list(m_value, sequence)
		for pair in list_of_max:
			target_index = pair[0]
			sequence[target_index] -= 1

			# print(f"Vertex Pairs({vertices[m_index]}, {vertices[target_index]})")

			neighbours = result[vertices[m_index]]
			neighbours.append(vertices[target_index])
			neighbours = result[vertices[target_index]]
			neighbours.append(vertices[m_index])

	return result