#Latihan
print ("Buat program meminta usia seseorang")
#Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia tersebut berdasarkan kriteria berikut: 
#0 - 12 tahun: Anak-anak 
#13 - 17 tahun: Remaja 
#18 - 59 tahun: Dewasa 
#60 tahun ke atas: lansia 

# Meminta input usia dari pengguna
usia = int(input("Masukkan usia Anda: "))

# Penentuan kategori berdasarkan rentang usia
if usia >= 0 and usia <= 12:
    print ("Anak-anak")
elif usia >= 13 and usia <= 17:
   print ("Remaja")
elif usia >= 18 and usia <= 59:
   print ("Dewasa")
elif usia >= 60:
    print ("Lansia")
else:
    print ("Usia tidak valid")
print ("Terima kasih sudah isi ya!")