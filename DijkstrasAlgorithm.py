def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    minDistances = []
	for index in range(len(edges)):
		traversed = [False for index in range(len(edges))]
		if index == start:
			minDistances.append(0)
		else:
			minDistance = None
			for pair in edges[start]:
				traversed[start] = True
				distance = explore(pair, index, edges, traversed)
				if distance > 0:
					if minDistance is None:
						minDistance = distance
					else:
						minDistance = min(minDistance, distance)
			if minDistance is None:
				minDistances.append(-1)
			else:
				minDistances.append(minDistance)
	return minDistances


def explore(pair, destination, edges, traversed):
	if traversed[pair[0]]:
		return -1
	if pair is None:
		return -1
	if pair[0] == destination:
		return pair[1]
	else:
		minDistance = None
		traversed[pair[0]] = True
		for edge in edges[pair[0]]:
			distance = explore(edge, destination, edges, traversed)
			if distance > 0:
				if minDistance is None:
					minDistance = distance
				else:
					minDistance = min(minDistance, distance)
		traversed[pair[0]] = False
		return minDistance + pair[1] if minDistance is not None else -1
