a = int(input('Masukkan jumlah data : '))
total = 0
for i in range(a):
    data= float(input(f'Masukkan data ke-{i+1}: '))
    total += data
rata_rata = total/a
print(f'rata-rata dari {a} data tersebut adalah = {rata_rata}')
