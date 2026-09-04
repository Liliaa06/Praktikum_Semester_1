print("Tugas Pertemuan 3")

Panjang = 12
Lebar = 5
Tinggi = 8

#Soal
#a. Hitunglah luas, volume dan keliling dari bangunan tersebut!
#b. Apakah luas bangunan tersebut lebih luas dari 50?
#c. Apakah volume tersebut bernilai 480?
#d. Jawab pertanyaan di atas menggunakan program

#a. Hitunglah luas, volume dan keliling dari bangunan tersebut! 
luas = 2 * ((Panjang * Lebar) + (Panjang * Tinggi) + (Lebar * Tinggi))
volume = Panjang * Lebar * Tinggi
keliling = 4 * (Panjang + Lebar + Tinggi)

print("\n=====Jawaban soal a=====")
print("Luas permukaan = ", luas, "cm^2") #tidak ada ketentuan satuan jadi permisalannya cm
print("Volume         = ", volume, "cm^3")
print("Keliling       = ", keliling, "cm")

#b. Apakah luas bangunan tersebut lebih luas dari 50?
print("\n=====Jawaban soal b=====")
if luas > 50:
    print("Luas bangunan lebih luas dari 50")
else:
    print("Luas bangunan tidak lebih luas dari 50")

#c. Apakah volume tersebut bernilai 480?
print("\n=====Jawaban soal c=====")
if volume == 480:
    print("Volume bangunan bernilai 480")
else:
    print("Volume bangunan tidak bernilai 480")

#c. Apakah volume tersebut bernilai 300? contoh lain jika yang muncul pada outputadalah kode false
print("\n=====Jawaban soal c=====")
if volume == 300:
    print("Volume bangunan bernilai 300")
else:
    print("Volume bangunan tidak bernilai 300")    