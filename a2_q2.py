def check_teams(graph, csp_sol):
	for i in csp_sol:
		for j in csp_sol:
			if i != j and csp_sol.get(i) == csp_sol.get(j):
				if graph.get(i).count(j) > 0:
					return False
	return True

def main():
	graph={0: [1, 2], 1: [0], 2: [0], 3: []}
	csp_sol={0:0, 1:1, 2:1, 3:0}
	print(check_teams(graph, csp_sol))


if __name__ == '__main__':
	main()

