# Remove Duplicates in-place from Sorted Array
temp = [1,1,2,2,2,3,3]

def removeDups(arr):
	n = len(arr)
	fin = [] 
	for i in range(n):
		if arr[i] not in fin:
			fin.append(arr[i])
	while len(fin) != n:
		fin.append("_")
	print(fin)

# we must do it inplace...
def inplaceDupsRemove(arr):
	st = set() 
	for i in arr:
		st.add(i)
	k = len(st)
	j = 0 
	for item in st:
		arr[j] = item 
		j += 1
	print(list(st))


if __name__ == '__main__':
	removeDups(temp)
	inplaceDupsRemove(temp)
