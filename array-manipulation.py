#Creates an new array
num = 8
array = [0]*num
print(array)

array = [i for i in range(num)]
print(array)

rows, cols = (5, 5)
array = [[i*j for i in range(cols)] for j in range(rows)]
print(array)

array = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(i + j**2 - 3)
    array.append(col)
print(array)

array = [[0]*rows]*cols
for row in array:
    print(row)

array = [[1,2,3],[3,4,5],[6,7,8]]
print("Before:")
for row in array:
    print(row)
array = [value for sublist in array for value in sublist]
print("After:")
print(array)

array = [[1,2,3],[4,5,6],[7,8,9]]
for row in array:
    for value in row:
        print(value, end=" ")
    print()

num = 2
column = [row[num] for row in array]
print(column)


