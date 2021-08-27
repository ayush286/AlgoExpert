#O(v + e) Time | O(v) space where v is the length of edges 
#and e edges in graph
def cycleInGraph(edges):
    # Write your code here.
	visitedNodes = [False for index in edges]
    for index in range(len(edges)):
		visitedNodes[index] = True
		isCycle = explore(index, edges, visitedNodes)
		if isCycle:
			return True
		visitedNodes[index] = False
	return False

def explore(index, edges, visitedNodes):
	for node in edges[index]:
		if visitedNodes[node]:
			return True
		else:
			visitedNodes[node] = True
			isCycle = explore(node, edges, visitedNodes)
			if isCycle:
				return True
		visitedNodes[node] = False
	return False
