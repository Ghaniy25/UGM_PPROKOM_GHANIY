# himpunan awal
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

# Selisih A & B
selisihAB = A.difference(B)
print("a. A difference B = ", selisihAB)

# Selisih B & A
selisihBA = B.difference(A)
print("b. B difference A = ", selisihBA)

# Selisih A & C
selisihAC = A.difference(C)
print("c. A difference C = ", selisihAC)

# Selisih B & C
selisihBC = B.difference(C)
print("d. B difference C = ", selisihBC)