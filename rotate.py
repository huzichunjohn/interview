#/usr/bin/env python
# -*- coding: utf-8 -*-

def rotate(matrix, row, column):
    # result = [[0 for i in range(row)] for j in range(column)]
    # for i in range(row):
    #     for j in range(column):
    #         result[column-j-1][i] = matrix[i][j]
    # return result

    result = []
    for j in range(column):
        output = [ matrix[i][column-j-1] for i in range(row)]
        result.append(output)
    return result

if __name__ == "__main__":
    mymatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print rotate(mymatrix, 4, 3)












