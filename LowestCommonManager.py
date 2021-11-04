#O(n) Time | O(d) Space, where n is total nodes and d is longest branch
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    ladderOne = orgTraversal(topManager, reportOne, [])
	ladderTwo = orgTraversal(topManager, reportTwo, [])
	idxOne = len(ladderOne) - 1
	idxTwo = len(ladderTwo) - 1
	if idxOne > idxTwo:
		return getLowestCommonManagerHelper(ladderTwo, ladderOne, idxTwo, idxOne)
	else:
		return getLowestCommonManagerHelper(ladderOne, ladderTwo, idxOne, idxTwo)
	
	
def getLowestCommonManagerHelper(ladderOne, ladderTwo, idxOne, idxTwo):
	# idxTwo is greater than idxOne
	while idxTwo > idxOne:
		idxTwo -= 1
	if ladderTwo[idxTwo] == ladderOne[idxOne]:
		return ladderTwo[idxTwo]
	while idxTwo > 0:
		idxTwo -= 1
		idxOne -= 1
		if ladderTwo[idxTwo] == ladderOne[idxOne]:
			return ladderTwo[idxTwo]
		
def orgTraversal(manager, reporter, ladder):
	ladder.append(manager)
	if manager.name == reporter.name:
		return ladder
	if len(manager.directReports) < 1:
		return ladder
	else:
		for subManager in manager.directReports:
			updatedLadder = orgTraversal(subManager, reporter, ladder)
			if updatedLadder[-1].name == reporter.name:
				return updatedLadder
			else:
				ladder.pop()
	return ladder


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
