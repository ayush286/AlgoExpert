#O(c*n) Time | O(c*n) Space, where c is capacity and n is items' length
def knapsackProblem(items, capacity):
    # Write your code here.
    n = len(items)
	table = [[0 for col in range(capacity + 1)] for row in range(n + 1)]
	for row in range(1, n + 1):
		for col in range(1, capacity + 1):
			table[row][col] = table[row - 1][col]
			if items[row - 1][1] <= col:
				table[row][col] = max(table[row][col], items[row - 1][0] + table[row - 1][col - items[row - 1][1]])
	return [table[-1][-1], getKnapsackItems(items, table)]


def getKnapsackItems(items, table):
	row = len(table) - 1
	col = len(table[0]) - 1
	itemsIndex = []
	while row > 0:
		if table[row][col] != table[row - 1][col]:
			itemsIndex.append(row - 1)
			col -= items[row - 1][1]
		row -= 1
	return list(reversed(itemsIndex))
			
