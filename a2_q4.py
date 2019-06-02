import random
import time
from csp import *

def rand_graph(n, p):
	graph = {}
	for i in range(n):
		graph[i] =[]

	for i in range(n):
		for j in range(n):
			if i != j:
				if p > random.random():
					if j not in graph[i]:
						graph[i].append(j)
						graph[i].sort()
					if i not in graph[j]:
						graph[j].append(i)
						graph[j].sort() 

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

def run_q4():
	graphs = [rand_graph(100, 0.1)] # Test
	for i in range(len(graphs)):
		result = {}
		variable = list(graphs[i].keys())
		domain = {}
		varLenth = len(variable)
		l = []
		timer = 0
		for j in range(varLenth):
			domain[j] = variable
		start_time = time.time()
		csp = CSP(variable, domain, graphs[i], different_values_constraint)
		result = min_conflicts(csp)
		elapsed_time = time.time() - start_time

		if result != None:
			timer = elapsed_time
			print(f'Total of assign: {csp.nassigns}')
			if check_teams(graphs[i], result):
				print(f'elapsed time (in seconds): {timer}')
				print(result)
				print()

	return

def main():
	run_q4()

if __name__ == '__main__':
	main()
