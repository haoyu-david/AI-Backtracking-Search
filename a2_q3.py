import random
import time
from csp import *

def rand_graph(n, p):
	graph = {}
	for i in range(n):
		graph[i] =[]

	for i in range(n):
		for j in range(i+1, n):
			if p > random.random():
				graph[i].append(j)
				graph[j].append(i)

	return graph

def check_teams(graph, csp_sol):
	for i in csp_sol:
		for j in csp_sol:
			if i != j and csp_sol.get(i) == csp_sol.get(j):
				if graph.get(i).count(j) > 0:
					return False
	return True


def run_q3():
	for i in range(5):
		print(f'Run: {i}')
		graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3), rand_graph(30, 0.4), rand_graph(30, 0.5)]		
		for graph in graphs:
			start_time = time.time()
			for j in range(30):
				domain = list(range(j))
				csp = MapColoringCSP(domain, graph)
				result = backtracking_search(csp, select_unassigned_variable=mrv, inference=forward_checking)
				if result != None:
					if check_teams(graph, result):
						elapsed_time = time.time() - start_time
						timer = elapsed_time
						print(f'Teams: {j}')
						print(f'Assigned: {csp.nassigns}')
						# print(f'Unassigned: {csp.unassigns}')
						print(f'elapsed time (in seconds): {timer}')
						print()
						break	
	return

def main():
	run_q3()

if __name__ == '__main__':
	main()