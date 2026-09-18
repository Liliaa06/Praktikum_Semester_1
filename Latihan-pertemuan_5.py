print ("Latihan soal pertemuan ke-5")

#Soal
#1. Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan! 
#2. Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan! 

print("\n=== BILANGAN GANJIL DAN GENAP (1 - 50) ===")

for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i} adalah bilangan GENAP")
    else:
        print(f"{i} adalah bilangan GANJIL")

print("\n=== BILANGAN PRIMA (1 - 100) ===")
for number in range(1, 101):
    # Bilangan prima harus lebih besar dari 1
    if number > 1:
        is_prima = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prima = False
                break
        
        if is_prima:
            print(number, end=" ")

print ("\nAlhamdulilah selesai")