def rotate(matrix):
    # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [[7,4,1],[8,5,2],[9,6,3]]
    # 3 6 9
    # row 0 col 0 = row 0 col 2
    # row 0 col 1 = row 1 col 2
    # row 0 col 2 = row 2 col 2
    temp = matrix[0][0]
    x = 0
    y = 0
    count = 0
    total_vals = len(matrix) ** 2
    
    while True:
        # x = y
        # y = len(matrix[0])-x-1
        x, y = y, len(matrix)-x-1
        matrix[x][y], temp = temp, matrix[x][y]
        count += 1
        if count == total_vals: return


        
        

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         temp = matrix[j][len(matrix[0])-i-1]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)