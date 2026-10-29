A = [9, 34, 59, 0, 10, 16, 45, 88]
print("Original List: ", A)

count = 0

for i in A:
    count += 1

    avg = count/len(A)

    print("Sum = ", count)
    print("Average = ", avg)

A.sort()

print("Smallest element is: ", A[0])

print("Largest element is: ", A[-1])