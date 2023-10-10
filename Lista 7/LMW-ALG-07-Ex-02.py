def symmetric_difference(M, N):
    diff_1 = M.difference(N)  
    diff_2 = N.difference(M)  
    symmetric_diff = diff_1.union(diff_2)
    return sorted(symmetric_diff)

M = {2, 4, 5, 9}
N = {2, 4, 11, 12}
result = symmetric_difference(M, N)
print(result)
