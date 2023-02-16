#!/usr/bin/python3
''' 0-rotate_2d_matrix task '''


def rotate_2d_matrix(matrix):
    ''' Given an n x n 2D matrix, rotate it 90 degrees clockwise. '''
    n = len(matrix[0])
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = temp
