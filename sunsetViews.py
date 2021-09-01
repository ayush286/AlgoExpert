#O(n) Time | O(n) Space where n is length of buildings array
def sunsetViews(buildings, direction):
	if len(buildings) < 1:
		return []
	if len(buildings) == 1:
		return [0]
    # Write your code here.
	viewBuildings = []
	if direction == "WEST":
		requiredHeight = buildings[0]
		viewBuildings.append(0)
		for index in range(1, len(buildings)):
			if buildings[index] > requiredHeight:
				requiredHeight = buildings[index]
				viewBuildings.append(index)
		return viewBuildings
	else:
		requiredHeight = buildings[len(buildings) - 1]
		viewBuildings.append(len(buildings) - 1)
		for index in reversed(range(len(buildings) - 1)):
			if buildings[index] > requiredHeight:
				requiredHeight = buildings[index]
				viewBuildings.append(index)
		viewBuildingsStack = []
		while viewBuildings:
			viewBuildingsStack.append(viewBuildings.pop())
		return viewBuildingsStack
