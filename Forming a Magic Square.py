def formingMagicSquare(s):
    # Brute force 
    magic_square = [
     [[8,1,6],[3,5,7],[4,9,2]]
    ,[[6,1,8],[7,5,3],[2,9,4]]
    ,[[4,9,2],[3,5,7],[8,1,6]]
    ,[[2,9,4],[7,5,3],[6,1,8]]
    ,[[8,3,4],[1,5,9],[6,7,2]]
    ,[[4,3,8],[9,5,1],[2,7,6]]
    ,[[6,7,2],[1,5,9],[8,3,4]]
    ,[[2,7,6],[9,5,1],[4,3,8]]
    
    ]

    given_square = [[4,9,2],[3,5,7],[8,1,5]]

    cost = []

    for i in range(8):
        sum = 0
        for j in range(3):
            for k in range(3):
                sum +=  abs(magic_square[i][j][k] - s[j][k])
        cost.append(sum)
            

    return min(cost)


print(formingMagicSquare([
    [2 ,5, 4],
    [4 ,6, 9],
    [4 ,5, 2],
]))

