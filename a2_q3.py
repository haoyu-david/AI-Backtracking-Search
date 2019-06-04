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
	groups={}
	for i in range(len(graph)):
		groups[i] = []
	for key, value in csp_sol.items():
		groups[value].append(key)
		groups[value].sort()
	for i in range(len(graph)):
		if groups[i] == []:
			groups.pop(i)
	print("Number of teams: {0}".format(len(groups)))

	for key, value in groups.items():
		for i in value:
			for j in value:
				if i != j:
					if graph[i].count(j) != 0:
						return False

	return True

def countGroup(csp_sol):
	groups={}
	for i in range(len(csp_sol)):
		groups[i] = []
	for key, value in csp_sol.items():
		groups[value].append(key)
		groups[value].sort()
	for i in range(len(csp_sol)):
		if groups[i] == []:
			groups.pop(i)
	print(f'Number of teams: {len(groups)}')
	return

def run_q3():
	for i in range(1):
		print(f'Run: {i}')
		graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3), rand_graph(30, 0.4), rand_graph(30, 0.5)]		
		for graph in graphs:
			start_time = time.time()
			for j in range(30):
				domain = list(range(j))
				csp = MapColoringCSP(domain, graph)
				result = backtracking_search(csp, select_unassigned_variable=mrv, inference=forward_checking)
				if result != None:
					elapsed_time = time.time() - start_time
					timer = elapsed_time
					print(f'Assigned: {csp.nassigns}')
					# print(f'Unassigned: {}')
					# if check_teams(graphs[i], result):
					print(f'elapsed time (in seconds): {timer}')
					print()
					break	
	return

def main():
	run_q3()

if __name__ == '__main__':
	main()