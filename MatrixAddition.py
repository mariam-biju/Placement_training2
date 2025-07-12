'''
Imagine you are helping a student with their mathematics homework which involves a lot of problems based on matrix addition. You decide to write a program to automate the task of adding two matrices, which would make the homework a breeze!
Write a program to add two matrices. The program should:
Prompt the user to enter the dimensions of the matrices (assume both matrices have the same dimensions).
Accept the elements of the two matrices from the user.
Display the two matrices.
Add the two matrices.
Print the resultant matrix.
Kindly check the sample test case for input and output format.

Input Format

2 2
1 2
3 4
5 6
7 8

Constraints

NA

Output Format

First Matrix:
1 2
3 4
Second Matrix:
5 6
7 8
Sum of the two matrices is:
6 8
10 12

Sample Input 0

2 2
1 2
3 4
5 6
7 8
Sample Output 0

First Matrix:
1 2 
3 4 
Second Matrix:
5 6 
7 8 
Sum of the two matrices is:
6 8 
10 12
Sample Input 1

1 1
6
8
Sample Output 1

First Matrix:
6
Second Matrix:
8
Sum of the two matrices is:
14
'''


rows,cols=map(int, input().split())

matrix1=[]
for _ in range(rows):
    row=list(map(int, input().split()))
    matrix1.append(row)

matrix2=[]
for _ in range(rows):
    row=list(map(int, input().split()))
    matrix2.append(row)

print("First Matrix:")
for row in matrix1:
    print(' '.join(map(str, row)))

print("Second Matrix:")
for row in matrix2:
    print(' '.join(map(str, row)))

sum_matrix=[]
for i in range(rows):
    row_sum=[]
    for j in range(cols):
        row_sum.append(matrix1[i][j]+matrix2[i][j])
    sum_matrix.append(row_sum)

print("Sum of the two matrices is:")
for row in sum_matrix:
    print(' '.join(map(str, row)))

