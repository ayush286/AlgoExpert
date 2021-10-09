#O(n) Time | O(n) Space, where n is length of path
def shortenPath(path):
    # Write your code here.
	directories = []
	isAbsolute = False
	if path[0] == '/':
		isAbsolute = True
	directory = ''
	directoryFound = False
	for index in range(len(path)):
		if path[index] == '/':
			if directoryFound:
				directories = addToDirectories(directory, directories, isAbsolute)
				directory = ''
				directoryFound = False
			else:
				directoryFound = True
				directories = addToDirectories(directory, directories, isAbsolute)
				directory = ''
		else:
			directory += path[index]
	directories = addToDirectories(directory, directories, isAbsolute)
	shortPath = '/' if isAbsolute else ''
	for folder in directories[:len(directories) - 1]:
		shortPath += folder + '/'
	if len(directories) < 1:
		return shortPath
	else:
		if path[-1] != '/':
			shortPath += directories[-1]
		else:
			shortPath += directories[-1] + '/'
		return shortPath

def addToDirectories(directory, directories, isAbsolute):
	#pop
	if directory == '..':
		if len(directories) < 1:
			if isAbsolute:
				return directories
			else:
				directories.append(directory)
				return directories
		else:
			if directories[-1] == '..':
				directories.append(directory)
				return directories
			else:
				directories.pop()
				return directories
	elif directory == '' or directory == '.':
		return directories
	else:
		directories.append(directory)
		return directories
