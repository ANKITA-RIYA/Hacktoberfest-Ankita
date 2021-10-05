def bubbleSorter(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

full_number_list=[2,4,5,31]
bubbleSorter(full_number_list)

print("The sorted list is given below:-")
for i in range(len(full_number_list)):
	print(full_number_list[i])
