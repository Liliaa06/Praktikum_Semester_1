print("Program 3.1 Menampilkan output dari operasi aritmatika sederhana")

#operasi aritmatika
a = 10
b = 3

#operasi tambah (+)
hasil_tambah = a + b
print(a,'+',b,'=',hasil_tambah)

#operasi kurang (-)
hasil_kurang = a - b
print(a,'-',b,'=',hasil_kurang)

#operasi perkalian (*)
hasil_kali = a * b
print(a,'*',b,'=',hasil_kali)

#operasi pembagian (/)
hasil_bagi = a / b
print(a,'/',b,'=',hasil_bagi)

#operasi eksponen (pangkat) **
hasil_eksponen = a ** b
print(a,'**',b,'=',hasil_eksponen)

#operasi modulus (%)
hasil_modulus = a % b
print(a,'%',b,'=',hasil_modulus)

#operasi floor division (//)
hasil_floor = a // b
print(a,'//',b,'=',hasil_floor)


print("\nProgram 3.2 konversi celcius ke satuan lain")
#latihan konversi satuan temperature

#program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input("Masukkan suhu dalam Celcius: "))
print("Suhu adalah", celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")

#fahrenheit
fahrenheit = (9/5) * celcius + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")


print("\n16Program 3.3 operasi komperasi")
#operai komperasi
#setiap hasil dari operasi komperasi adalah boolean
#>,<,>=,<=,==,!=,is, is not

a = 4
b = 2

#lebih besar dari >
print("=============== lebih besar dari (>)")
hasil = a > 3
print(a,'>',b,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

#kurang dari <
print("=============== kurang dari (<)")
hasil = a < 3
print(a,'<',b,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

#lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,'>=',b,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

#kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,'<=',b,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

#sama dengan ==
print("=============== sama dengan (==)")
hasil = a == 4
print(a,'==',b,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

#tidak sama dengan !=
print("=============== tidak sama dengan (!=)")
hasil = a != 4
print(a,'!=',b,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

#'is' sebagai komparasi obj identity (bukan literal)
x = 5 #ini adalah assigment membuat object
y = 5
hasil = x is not y
print('x is not y =', hasil)

