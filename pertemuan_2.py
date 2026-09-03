print("TUGAS");
print("\nI. Daftar nama")
#Deklarasi variabel sesuai dengan data Anda
nama = "Ucup Santoso"
umur = 200
berat = 56.4
#Menampilkan output
print("Nama  :",(nama))
print(f"Umur  : {umur} tahun")
print(f"Berat : {berat} kg")

print("\nII. Ubah tipe data")
#Variabel awal
angka_string = "123"
#Konversi string menjadi integer
data_int = int (angka_string)
print("1. data = ", data_int, ",type = ", type (data_int))
angka_float = 45.67
#Konversi float menjadi integer
data_int = int (angka_float)
print("2. data = ", data_int, ",type = ", type (data_int))
angka_integer = 89
#Konversi integer menjadi float
data_float = float (angka_integer)
print("3. data = ", data_float, ",type = ", type (data_float))
#Konversi integer menjadi string
data_str = str (angka_integer)
print ("4. data = ", data_str, ",type = ", type (data_str))

print("\nIII. Input data dari user")
#a. Meminta input usia (int)
usia = int(input("a. Masukan usia Anda: "))
print("data ",usia,",type =",type(usia))
#b. Meminta input tinggi badan (float)
tinggi_badan = float(input("b. Masukan tinggi badan Anda: "))
print("data ",tinggi_badan, ",type =",type(tinggi_badan))
#c. Meminta input nama (string)
nama = (input("c. Masukan nama Anda: "))
print("data ",nama,",type =",type(nama))
#ini opsional untuk Menampilkan kembali hasil input untuk memastikan data tersimpan
print("\n--- Data yang Berhasil Disimpan ---")
print(f"Nama         : {nama}")
print(f"Usia         : {usia} tahun")
print(f"Tinggi Badan : {tinggi_badan} cm")