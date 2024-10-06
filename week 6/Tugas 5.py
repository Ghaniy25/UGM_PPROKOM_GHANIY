# himpunan awal
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

# Komplemen A & B
komplemenAB = A.symmetric_difference(B)
print("a. A symmetric difference B = ", komplemenAB)

# Komplemen B & A
komplemenBA = B.symmetric_difference(A)
print("b. B symmetric difference A = ", komplemenBA)

# Komplemen A & C
komplemenAC = A.symmetric_difference(C)
print("c. A symmetric difference C = ", komplemenAC)

# Komplemen B & C
komplemenBC = B.symmetric_difference(C)
print("b. B symmetric difference A = ", komplemenBC)