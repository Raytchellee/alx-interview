def pascal_triangle(n):
    if n <= 0:
        return []
    
    res = [[1]]
    
    for idx in range(1, n):
        temp = []
        length = len(res[idx - 1])
        
        for i in range(length):
            if i == 0:
                temp.append(res[idx - 1][0])
            if 0 < i < length:
                temp.append(res[idx - 1][i - 1] + res[idx - 1][i])
            if i == length - 1:
                temp.append(res[idx - 1][length - 1])
        
        res.append(temp)
    
    return res
