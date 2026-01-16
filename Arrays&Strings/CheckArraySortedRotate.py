# LC 1752 
"""
We are supposed to check if the given array is sorted and rotated.
rotations can be anything like 0,1,2...n times
"""

temp = [3,4,5,1,2]

# if 1 loop violation, i.e, arr[i] > arr[i+1], it is valide
# only 0 or 1 loop violation is valid.

def checkSortedRotated(arr):
	n = len(arr)
	def is_sorted(arr):
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				return False
		return True

	for k in range(n):
		rotated = arr[k:] + arr[:k]
		if is_sorted(rotated):
			return True 
	return False

def optimizedSortRotate(arr):
	n = len(arr)
	counter = 0 
	for i in range(n-1):
		if arr[i] > arr[i+1]:
			counter += 1
		elif arr[-1] > arr[0]:
			counter += 1
	if counter <= 1:
		print("SORTED")
	else:
		print("NOT SORTED")

if __name__ == '__main__':
	if checkSortedRotated(temp):
		print("Sorted and rotated")
	else:
		print("NOPE")
	print("Sorted and rotated")