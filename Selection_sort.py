#Python program for Selection sort
#sample array
A = [43, 58, 29, 78, 36]
for i in range(len(A)):
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j		
	A[i], A[min_idx] = A[min_idx], A[i]
for i in range(len(A)):
	print("%d" %A[i]),
