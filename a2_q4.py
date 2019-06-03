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
	for run in range(5):
		print(f'Run: {run}')
		graphs = [rand_graph(100, 0.1), rand_graph(100, 0.2), rand_graph(100, 0.3), rand_graph(100, 0.4), rand_graph(100, 0.5)]
		for i in range(len(graphs)):
			result = {}
			variable = list(graphs[i].keys())
			domain = {}
			domainLen = 0
			varLenth = len(variable)
			timer = 0
			start_time = time.time()
			while domainLen <= varLenth:
				l = []
				for j in range(domainLen):
					l.append(j)
				for k in range(varLenth):
					domain[k] = l
			
				csp = CSP(variable, domain, graphs[i], different_values_constraint)
				try:
					result = min_conflicts(csp)
				except:
					domainLen += 10
					continue

				if bool(result):
					elapsed_time = time.time() - start_time
					timer = elapsed_time
					if check_teams(graphs[i], result):
						print(f'Total of assign: {csp.nassigns}')
						print(f'elapsed time (in seconds): {timer}')
						# print(result)
						print()
						break
				else:
					domainLen += 10

	return

def main():
	run_q4()

if __name__ == '__main__':
	main()
