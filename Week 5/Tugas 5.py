# Deklarasi variabel
var_nilai = 0
var_i = 1

# Perulangan FOR
for var_nilai in range(0, 10):
    print("Perulangan pertama Ke ", var_nilai)
    
    # Perulangan kedua di dalam perulangan pertama
    for var_i in range(1, 3):
        print(" Perulangan ke ", var_nilai, ", ", var_i)
        
    # var_i di luar perulangan var_i
    var_i = 1

# Di luar perulangan var_nilai
print("var_nilai = ", int(var_nilai) + 1, " = 10. Bernilai False")