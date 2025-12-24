import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a[0,2]) 
print(a[:,1]) #get column
print(a[1,1:3]) #get section

b = np.zeros((3,3,3))
print(b)
b = np.ones((2,2), dtype="int32")
print(b)
b = np.full((3,3), 42, dtype="float32")
print(b)

#Random numbers
b = np.random.rand(4,2)
print(b)

b = np.random.randint(12, size=(3,3)) #0-12 size 3x3
print(b)

# Identity matrix X by X
b = np.identity(5)
print(b)

# Repeat
b = np.array([[1,2,3]])
a = np.repeat(b, 3, axis=0)
print(a)

# Create Unique
a = np.ones((5,5))
b = np.zeros((3,3))
b[1,1] = 9
a[1:4,1:4] = b
print(a)

# copying points to same address space
a = np.array([1,2,3])
b = a
b[1] = 5
print(a)

# copying to unique address space
a = np.array([1,2,3])
b = a.copy()
b[1] = 5
print(a)

# math
print(a + 2)
print(a - 2)
print(a / 2)
a = a - 2
print(a)

a = np.array([1,2,3])
b = np.array([2,3,4])

print(a+b)
print(a*b)
print(np.cos(a))

# Matrix multiplication
a = np.ones((2,5))
b = np.full((5,3), 3)
print(a)
print(np.matmul(a, b))

# determinant
a = np.identity(3)
print(np.linalg.det(a))

# other functions
a = np.random.randint(12, size=(5,5))
print(a)
print("min axis 1 = " + str(np.min(a, axis=1)))
print("max = " + str(np.max(a)))
