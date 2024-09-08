pilihan1= str(input("pilihan 1 (Batu, Kertas, Gunting) ="))
pilihan2= str(input("pilihan 2 (Batu, Kertas, Gunting) ="))
print(f"User 1={pilihan1}")
print(f"User 2={pilihan2}")

if pilihan1 == pilihan2:
        print("Hasil = Draw")
elif(pilihan1 == "Batu" and pilihan2 == "Gunting"):
    print("User 1 = You WIN")
elif(pilihan1 == "Gunting" and pilihan2 == "Kertas"):
    print("User 1 = You WIN")
elif(pilihan1 == "Kertas" and pilihan2 == "Batu"):
    print("User 1 = You WIN")
else:
    print("User 2 = You WIN")