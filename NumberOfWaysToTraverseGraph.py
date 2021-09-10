# O(w + h) Time | O(1) Space, where w and h are input width and height
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
	denmoniator = getFactorial(width - 1) * getFactorial(height - 1)
    return getFactorial(width + height - 2)/denmoniator

def getFactorial(number):
	factorial = 1
	while number > 0:
		factorial *= number
		number -= 1
	return factorial
