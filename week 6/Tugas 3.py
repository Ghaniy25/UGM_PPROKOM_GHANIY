# himpunan awal
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

# Irisan A & B
IrisanAB = A.intersection(B)
print("a. A ∩ B = ",IrisanAB)

# Irisan B & D
IrisanBD = B.intersection(D)
print("b. B ∩ D = ", IrisanBD)

# Irisan C & D
IrisanCD = C.intersection(D)
print("c. C ∩ D = ", IrisanCD)

# Irisan A & B & C & D
IrisanABCD = A.intersection(B,C,D)
print("d. A ∩ B ∩ C ∩ D = ", IrisanABCD) 