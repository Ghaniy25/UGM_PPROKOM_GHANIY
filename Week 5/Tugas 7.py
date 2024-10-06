# Deklarasi variabel
var_nilai = 0

# Perulangan FOR
for var_nilai in range(0, 10):
    print("Perulangan pertama Ke ", var_nilai)
    
    # Reset var_i sebelum perulangan while dimulai
    var_i = 1
    
    # Perulangan WHILE di dalam perulangan FOR
    while var_i < 3:
        print(" Perulangan ke ", var_nilai, ", ", var_i)
        var_i += 1

# Di luar perulangan var_nilai
print("var_nilai = ", int(var_nilai) + 1, " = 10. Bernilai False")