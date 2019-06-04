import random

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

def main():
	print(rand_graph(10, 0.1))


if __name__ == '__main__':
	main()