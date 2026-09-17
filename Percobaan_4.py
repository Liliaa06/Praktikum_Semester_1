print("\nProgram 4.1 Logical\n")
#operasi logika atau boolean
#not, or, and, xor

print("=============== not")
a = True
b = not a
print ('data a = ', a)
print ('---------- NOT')
print ('data b =' ,b)

#OR (jika salah satu true, maka hasilnya adalah true)
print ('===OR===')
a = False
b = False
c = a or b
print (a, 'OR' ,b, '=', c)
a = False
b = True
c = a or b
print (a, 'OR' ,b, '=', c)
a = True
b = False
c = a or b
print (a, 'OR' ,b, '=', c)
a = True
b = True
c = a or b
print (a, 'OR' ,b, '=', c)

#AND (jika dua buah nilai true, maka hasilnya true)
print ('===AND===')
a = False
b = False
c = a and b
print (a, 'AND' ,b, '=', c)
a = False
b = True
c = a and b
print (a, 'AND' ,b, '=', c)
a = True
b = False
c = a and b
print (a, 'AND' ,b, '=', c)
a = True
b = True
c = a and b
print (a, 'AND' ,b, '=', c)

#XOR (akan menghasilkan true jika salah satu true, sisanya false) 
print ('===XOR===')
a = False
b = False
c = a ^ b
print (a, 'XOR' ,b, '=', c)
a = False
b = True
c = a ^ b
print (a, 'XOR' ,b, '=', c)
a = True
b = False
c = a ^ b
print (a, 'XOR' ,b, '=', c)
a = True
b = True
c = a ^ b
print (a, 'XOR' ,b, '=', c)

print ("\n\nProgram 4.2 logika dan komparasi\n")
#latihan logika dan komparasi 
#membuat gabungan area rentang dari angka
#++++++3--------10++++++

inputUser = float(input("masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n:"))

#=++++++3-------- 
#
isKurangDari = (inputUser < 3)
print ("Kurang dari 3 =", isKurangDari)

#=--------10++++++
#memeriksa angka lebih besar dari 10
isLebihDari = (inputUser > 10)
print ("Lebih dari 10 =", isLebihDari)
isCorrect = isKurangDari or isLebihDari
print ("angka yang anda masukan:", isCorrect)

print ("=========================")

#------3+++++10------
#kasus irisan 

inputUser = float(input("masukan angka yang bernilai \nlebih dari 3 \natau \nkurang dari 10\n:"))

#------3++++++++++
#lebih dari 3
isLebihDari = inputUser > 3
print ("Lebih dari 3 =", isLebihDari)

#++++++++++10------
#kurang dari 10
isKurangDari = inputUser < 10
print ("Kurang dari 10 =", isKurangDari)
isCorrect = isLebihDari and isKurangDari
print ("angka yang anda masukan:", isCorrect)

print ("\n\nProgram 4.3 IF and ELSE\n")

#if dan else statement

#1. if nya
#2. kondisinya
#3. aksinya

nama = input ("Siapa nama anda? ")

#1. program if inline
if nama == "Amallia":
    print ("Hai Amallia, si imyut!")
else:
    print ("Ah! kamu bukan Amallia")
print ("Akhir dari program\n")

print ("\nProgram 4.4 ELIF statement\n")
#ELIF = else if statement

nama = input("siapa nama anda? ")

#if kondisi:
#    aksi true
# elif kondisi: 
#    aksi true 
#elif kondisi: 
#    aksi true 
# else: 
#    aksi 

if nama == "Amallia": #kondisi 1
    print ("Hai Amallia, si imyut!") #aksi true
elif nama == "Putri": #konndisi 2
    print ("Hai Putri, si cantik!")
elif nama == "Nurul": #kondisi 3
    print ("Hai Nurul, kamu sehat selalu ya!!")
else:
    print ("Lu siapa nyak??")
print ("Akhir dari program")