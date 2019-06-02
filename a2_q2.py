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

	for key, value in groups.items():
		for i in value:
			for j in value:
				if i != j:
					if graph[i].count(j) != 0:
						return False

	return True

def main():
	graph={0: [1, 2], 1: [0], 2: [0], 3: []}
	csp_sol={0:0, 1:1, 2:1, 3:0}
	print(check_teams(graph, csp_sol))


if __name__ == '__main__':
	main()

