N=200000
A=60*60*24
HARI=N//A
B=A*HARI
C=N-B
JAM=C//(60*60)
D=JAM*(60*60)
E=C-D
MENIT=E//60
DETIK=E%60
print(f"{HARI} hari {JAM} jam {MENIT} menit {DETIK} detik")
