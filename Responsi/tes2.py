from tracemalloc import start
from ai_pkg.search import *

# Post
city_map = Graph(dict(
        Kota_A=dict(Kota_B=1000, Kota_C=1000, Kota_D=1000),
        Kota_B=dict(Kota_E=1000, Kota_F=1000),
        Kota_C=dict(Kota_T=1000, Kota_H=1000),
        Kota_D=dict(Kota_I=1000, Kota_T=1000),
        Kota_F=dict(Kota_T=1000, Kota_G=1000),
        Kota_H=dict(Kota_T=1000)),
directed=True)
city_map = Graph(dict(
        Frankfurt=dict(Mannheim=85, Wurzburg=217, Kassel=173),
        Mannheim=dict(Karlsruhe=80),
        Wurzburg=dict(Erfurt=186, Numberg=103),
        Karlsruhe=dict(Augsburg=250),
        Numberg=dict(Stuttgart=183, Munchen=167),
        Augsburg=dict(Munchen=84),
        Munchen=dict(Augsburg=84, Numberg=167, Kassel=502),
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

def breadth_first_search(problem):
    global track_path
    frontier = deque([Node(problem.initial)])
    explored = set()
    track_path = [problem.initial]
    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        expanded = node.expand(problem)
        for child in expanded:
            track_path.append(child.state)
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

def depth_first_search(problem):
    global track_path
    frontier = [(Node(problem.initial))]  # Stack
    explored = set()
    track_path = [problem.initial]
    child_travel = [(Node(problem.initial))]
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        # frontier.extend(child for child in node.expand(problem)
        #                 if child.state not in explored and child not in frontier)
        expanded = node.expand(problem)
        for child in expanded:
            print(child.state)
            # if (node.state == problem.initial):
            #     track_path.append(child.state)
            #     frontier.append(child)
            # else:  
            track_path.append(child.state)
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
            frontier.append(child)
    return None
    




if __name__=='__main__':
    # Post
    # start = 'Kota_A'
    # tujuan 1
    # goal = 'Kota_H'
    # tujuan 2
    # goal = 'Kota_G'
    # tujuan 3
    # goal = 'Kota_I'
    start = 'Frankfurt'
    goal = 'Stuttgart'
    track_path = []
    romania_problem = CityProblem(start, goal , city_map)
    # node = breadth_first_search(romania_problem)
    node = depth_first_search(romania_problem)
    if node is not None:
        final_path = node.solution()
        final_path.insert(0, start)
        print('TRACKING PATH: ', ' -> '.join(track_path))
        print('SOLUTION PATH: ', ' -> '.join(final_path))