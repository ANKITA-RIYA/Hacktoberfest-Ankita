input_str = input('Enter elements of a list separated by space ')
print("\n")
arr= input_str.split()   #to convert the input string to list

print('array is: ', arr)

for i in range(len(arr)):     #to convert each element to integer type
    arr[i] = int(arr[i])

#function definition for bubble sort 
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("% d" % arr[i], end=" ")
