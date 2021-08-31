#O(n) Time | O(n) Space where n is length of array
def nextGreaterElement(array):
    # Write your code here.
	if len(array) < 1:
		return []
	if len(array) < 2:
		return [-1]
	stack = []
	outputs = [None for elem in array]
	for index in range(1, len(array)):
		if stack:
			while len(stack) > 0 and array[stack[-1]] < array[index]:
					outputs[stack.pop()] = array[index]
		if array[index - 1] < array[index]:
			outputs[index - 1] = array[index]
		else:
			stack.append(index - 1)
	stack.append(len(array) - 1)
	stackSize = len(stack)
	traverseStack(array, stack, outputs)
	newStackSize = len(stack)
	while stack and stackSize != newStackSize:
		stackSize = len(stack)
		traverseStack(array, stack, outputs)
		newStackSize = len(stack)
	if stack:
		while len(stack) > 0:
			outputs[stack.pop()] = -1
    return outputs

def traverseStack(array, stack, outputs):
	if not stack:
		return
	startIndex = stack[-1]
	nextIndex = (startIndex + 1) % len(array)
	counter = 0
	while stack and counter < len(array):
		if array[stack[-1]] < array[nextIndex]:
			outputs[stack[-1]] = array[nextIndex]
			stack.pop()
		else:
			nextIndex += 1
			nextIndex %= len(array)
		counter += 1
