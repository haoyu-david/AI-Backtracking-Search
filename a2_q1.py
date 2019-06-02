import random

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

def main():
	print(rand_graph(10, 0.1))


if __name__ == '__main__':
	main()