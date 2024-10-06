# himpunan awal
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

# Gabungan A & B
GabunganAB = A.union(B)
print("a. A U B = ", GabunganAB)

# Gabungan B & C
GabunganBC = B.union(C)
print("b. B U C = ", GabunganBC)

# Gabungan B & C & D
GabunganBCD = B.union(C,D)
print("c. B U C U D = ", GabunganBCD)

# Gabungan A & B & C & D
GabunganABCD = A.union(B,C,D)
print("d. A U B U C U D = ", GabunganABCD)