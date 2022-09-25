#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix)):
            if j == len(matrix):
                print(matrix[i][j])
            else:
                print(matrix[i][j], end=" ")
        print()
    if matrix == [[]]:
        print()
