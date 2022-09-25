#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix)):
            if j == (len(matrix) - 1):
                print(matrix[i][j])
            else:
                print(matrix[i][j], end=" ")
    if matrix == [[]]:
        print()
