def sortStack(stack):
    # Write your code here.
	if len(stack) < 1:
		return stack
    return sortStackHelper(stack)
#O(n^2) Time | O(n) Space where n is length of stack
def sortStackHelper(stack):
	if len(stack) == 1:
		return stack
	top = stack.pop()
	stack = sortStackHelper(stack)
	if stack[-1] <= top:
		stack.append(top)
		return stack
	else:
		while top is not None:
			temp = stack.pop()
			stack.append(top)
			stack = sortStackHelper(stack)
			top = temp
			if stack[-1] <= top:
				stack.append(top)
				top = None
				return stack
	return stack
				
