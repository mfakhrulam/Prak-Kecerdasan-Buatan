from ai_pkg.search import Graph, Problem, Node
from ai_pkg.utils import random, argmax_random_tie

city_map = Graph(dict(
	Oradea=dict(Oradea=0, Sibiu=24, Arad=59, Zerind=38),
	Sibiu=dict(Oradea=34, Sibiu=0, Arad=51, Zerind=56),
	Arad=dict(Oradea=59, Sibiu=51, Arad=0, Zerind=47),
	Zerind=dict(Oradea=38, Sibiu=56, Arad=47, Zerind=0)),
	directed=False)

distances = {}
# TSP program Diberikan daftar kota dan jarak antara setiap pasangan kota, 
# apa rute terpendek yang mungkin mengunjungi setiap kota tepat satu kali dan kembali ke kota asal
class TSP_problem(Problem):
	def generate_neighbour(self, state):
		neighbour_state = state[:]
		left = random.randint(0, len(neighbour_state)-1)
		right = random.randint(0, len(neighbour_state)-1)
		if left > right:
			left, right = right, left
		neighbour_state[left: right + 1] = reversed(neighbour_state[left: right + 1])
		return neighbour_state

	def actions(self, state):
		return [self.generate_neighbour]

	def result(self, state, action):
		return action(state)

	def path_cost(self, state):
		cost = 0
		for i in range(len(state)-1):
			current_city = state[i]
			next_city = state[i+1]
			cost += distances[current_city][next_city]
		cost += distances[state[0]][state[-1]]
		return cost

	def value (self, state):
		return -1*self.path_cost(state)

def hill_climbing(problem):
	def find_neighbors(state, number_of_neighbors=100):
		neighbors = []
		for i in range(number_of_neighbors):
			new_state = problem.generate_neighbour(state)
			neighbors.append(Node(new_state))
			state =  new_state
		return neighbors

	current = Node(problem.initial)
	while True:
		neighbors = find_neighbors(current.state)
		if not neighbors:
			break
		neighbor = argmax_random_tie(neighbors, key=lambda node: problem.value(node.state))
		if problem.value(neighbor.state) <= problem.value(current.state):
			break
		current.state = neighbor.state
	return current.state
