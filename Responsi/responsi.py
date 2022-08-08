# Nama : Muhammad Fakhrul Amin
# NIM  : 2000018277

from ai_pkg.search import *

start = 'Frankfurt'
goal = 'Numberg'

city_map = Graph(dict(
        Frankfurt=dict(Kassel=173, Wurzburg=217, Mannheim=85), # kassel dan mannheim tak balik
        # Frankfurt=dict(Mannheim=85, Wurzburg=217, Kassel=173), # awal
        Mannheim=dict(Karlsruhe=80),
        Wurzburg=dict(Erfurt=186, Numberg=103),
        Karlsruhe=dict(Augsburg=250),
        Numberg=dict(Stuttgart=183, Munchen=167),
        Augsburg=dict(Munchen=84),
        # Munchen=dict(Numberg=167, Augsburg=84, Kassel=502), # numberg dan augsburg tak balik
        # Munchen=dict(Augsburg=84, Numberg=167, Kassel=502), # awal
        Kassel=dict(Munchen=502)),
directed=True)

class CityProblem(Problem):
    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph
    def actions(self, A):
        return list(self.graph.get(A).keys())
    def result(self, state, action):
        return action
    def path_cost(self, cost, A, action, B):
        return cost + (self.graph.get(A, B) or infinity)

def depth_first_search(problem):
    global track_path
    frontier = [(Node(problem.initial))]  # Stack
    explored = set()
    # track_path = [problem.initial] # awal
    track_path = [] # ngide
    while frontier:
        # print(frontier)
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        expanded = node.expand(problem)
        track_path.append(node.state) # ngide

        for child in expanded:
            # track_path.append(child.state) # awal
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    # print(child)
                    track_path.append(child.state) # ngide
                    return child
            frontier.append(child)
    return None
    
if __name__=='__main__':
    track_path = []
    romania_problem = CityProblem(start, goal , city_map)
    node = depth_first_search(romania_problem)
    print('Kota asal   :', start)
    print('Kota tujuan :', goal)
    if node is not None:
        final_path = node.solution()
        final_path.insert(0, start)
        print('TRACKING PATH: ', ' -> '.join(track_path))
        print('SOLUTION PATH: ', ' -> '.join(final_path))