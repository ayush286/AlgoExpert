#O(nlogn) Time | O(n) space where n is length of tasks
def taskAssignment(k, tasks):
    # Write your code here.
	sortedTasks = []
	assignedTasks = []
	for task in tasks:
		sortedTasks.append(task)
	sortedTasks.sort()
	left = 0
	right = len(tasks) - 1
	while left < right:
		currentTask = []
		task1Idx = tasks.index(sortedTasks[left])
		currentTask.append(task1Idx)
		tasks[task1Idx] *= -1
		task2Idx = tasks.index(sortedTasks[right])
		currentTask.append(task2Idx)
		tasks[task2Idx] *= -1
		assignedTasks.append(currentTask)
		left += 1
		right -= 1
	return assignedTasks
