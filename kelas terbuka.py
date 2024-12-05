                                                                      ###variable### EPS.4
print("\n==========PROGRAM VARIABEL==========\n")
print('''
perumpamaannya : variabel adalah wadah
''')                                                                       
nama = 'beel' #variabel berisi srting harus menggunakan kutip1
print(nama)
umur = 18
print("namaku :",nama,", umurku :",umur,"tahun.")

                                                           ###tipe data### EPS.5

#kumpulan karakter / string
print("\n==========PROGRAM TIPE DATA STRING==========\n")
data_string = 'hallo'
print('data : ',data_string)
print("-bertipe : ", type(data_string))


#integer
print("\n==========PROGRAM TIPE DATA INTEGER==========\n")
data_integer = 15
print('data : ',data_integer)
print("-bertipe : ", type(data_integer))


#float
print("\n==========PROGRAM TIPE DATA FLOAT==========\n")
data_float = 15.0
print('data : ',data_float)
print("-bertipe : ", type(data_float))

#biner : true,false /bollean
print("\n==========PROGRAM TIPE DATA BOOLEAN==========\n")
data_bool = False
print('data : ',data_bool)
print("-bertipe : ", type(data_bool))


                                                                                    ###CASTING TIPE DATA### EPS.6

print("\n==========PROGRAM MENGUBAH TIPE DATA KE TIPE DATA YANG LAIN==========\n")

##DATA INTEGER
print("ubah dari integer : ")
data_int = 9;
print ("data = ", data_int, ",type =",type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool =bool(data_int)
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

##DATA FLOAT
print("ubah dari float : ")
data_float = 15.5
print ("data = ", data_float, ",type =",type(data_float))
data_int = int(data_float)
data_str = str(data_float)
data_bool =bool(data_float)
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

##DATA BOOLEAN
print("ubah dari boolean : ")
data_bool = True #analisis true sama false nya
print ("data = ", data_bool, ",type =",type(data_bool))
data_int = int(data_bool)
data_str = str(data_bool)
data_float =bool(data_bool)
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_float, ",type =",type(data_float))

##DATA STRING
print("ubah dari string : ")
data_string = 10 #jika di isi kalimat akan eroor(ANALISIS DI BAGIAN BOOLEAN)            
print ("data = ", data_string, ",type =",type(data_string))
data_int = int(data_string)
data_float = str(data_string)
data_bool =bool(data_string)
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_bool, ",type =",type(data_bool))

                                                                                    ###mengambil nilai input### EPS.7
print("\n==========PROGRAM MENGAMBIL INPUT==========\n")
input("data input yang membebaskan user memasukan nilai, contoh :")






                                                                                      ###ARITMATIKA### EPS.8

a = 10
b = 3
hasil = a + b

#penjumlahan
print("\n==========PROGRAM PENJUMLAHAN==========\n")
print(a,"+",b,"=",hasil)

#pengurangan
print("\n==========PROGRAM PENGURANGAN==========\n")
hasil = a - b
print(a,"-",b,"=",hasil)

#perkalian
print("\n==========PROGRAM PERKALIAN==========\n")
hasil = a * b
print(a,"*",b,"=",hasil)

#pembagian
print("\n==========PROGRAM PEMBAGIAN==========\n")
hasil = a / b
print(a,"/",b,"=",hasil)

#exsponen/pangkat
print("\n==========PROGRAM EXSPONEN==========\n")
hasil = a ** b
print(a,"**",b,"=",hasil)

#modulus/sisa dari pembagian
print("\n==========PROGRAM MODULUS==========\n")
hasil = a % b
print(a,"%",b,"=",hasil)

#floor division/kebalikan modulus 
print("\n==========PROGRAM FLOOR DIVISON==========\n")
hasil = a // b
print(a,"//",b,"=",hasil) #hasilnya dibulatkan ke bawah

#proritas operasi
print("\n==========PROGRAM PRIORITAS OPERASI==========\n")
'''
1. ()
2. exponen
3. perkalian dkk * / ** % //
4. pertambahan & pengurangan + -
'''
a = 5
b = 10
c = 15
d = 20
hasil = a ** b * c + a / b - b % c // a
print(a,'**',b,'*',c,'+',a,'/',b,'-',b,'%',c,'//',a,'=',hasil)

#kurung akan mengambil langkah paling pertama
print("\n==========PROGRAM PRIORITAS OPERASI 'KURUNG AKAN MENGAMBIL LANGKAH PERTAMA'==========\n")
hasil = (a + b) * c
print("(",a,"+",b,")","*",c,"=",hasil)



                                                                    ###latihan konversi satuan temperature### EPS.9

#program konversi celsius ke satuan lain

print("\n==========PROGRAM KONVERSI TEMPERATUR==========\n")
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukan suhu celcius : '))
print("suhu adalah : ",celcius,"celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah : ",reamur,"Reamur")

#fahreinheit
fahreinheit = ((9/5) * celcius) + 32
print("suhu dalam Fahreinheit adalah : ",fahreinheit,"Fahreinheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam Kelvin adalah : ",kelvin,"kelvin")



                                                                                    ###operasi komparasi### EPS.10
#setiap hasil dari komparasi adalah boolean
#>,<,>=,<=,==,!=,is,is not

a = 4
b = 2
##lebih dari & kurang dari tidak dimulai dari titik pas
# lebih dari >
print("\n==========PROGRAM LEBIH DARI==========\n")
hasil  = a > 3
print(a,'>',3,'=',hasil)

#kurang dari <
print("\n==========PROGRAM KURANG DARI==========\n")
hasil  = a < 3
print(a,'<',3,'=',hasil)

##lebih dari sama dengan & kurang dari sama dengan dimulai dari titik pas

#lebih dari sama dengan
print("\n==========PROGRAM LEBIH DARI SAMA DENGAN==========\n")
hasil  = a >= 3
print(a,'>=',3,'=',hasil)

#kurang dari sama dengan
print("\n==========PROGRAM KURANG DARI SAMA DENGAN==========\n")
hasil  = a <= 3
print(a,'<=',3,'=',hasil)

#sama dengan
print("\n==========PROGRAM SAMA DENGAN==========\n")
hasil  = a == 3
print(a,'==',3,'=',hasil)

#tidak sama dengan
print("\n==========PROGRAM TIDAK SAMA DENGAN==========\n")
hasil = a != 3
print(a,'!=',3,'=',hasil)
 
# 'is' sebagai komparasi object identity
print("\n==========PROGRAM IS / SAMA DENGAN==========\n")
a = 5 # ini adalah assignment membut object 
b = 5
print('nilai a =,',a,',id = ',hex(id(a)))
print('nilai b =,',b,',id = ',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

# 'is not' sebagai komparasi object identity
print("\n==========PROGRAM IS NOT / TIDAK SAMA DENGAN==========\n")
a = 5 # ini adalah assignment membut object 
b = 5
print('nilai a =,',a,',id = ',hex(id(a)))
print('nilai b =,',b,',id = ',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

                                                                            ###operasi logika = bolean### EPS.11
print("\n==========OPERASI LOGIKA = BOOLEAN==========\n")

# Hukum Boolean :  
# Hukum Komutatif (Commutative Laws) :: A AND B = B AND A || A OR B = B OR A 
# Hukum Asosiatif (Associative Laws) :: (A AND B) AND C = A AND (B AND C) || (A OR B) OR C = A OR (B OR C)
# Hukum Distributif (Distributive Laws) :: A AND (B OR C) = (A AND B) OR (A AND C) || A OR (B AND C) = (A OR B) AND (A OR C)
# Hukum Double Negasi (Double Negation Law) :: NOT (NOT A) = A
# Hukum Absorpsi (Absorption Laws) :: A AND (A OR B) = A || A OR (A AND B) = A
# Hukum De Morgan (De Morgan's Laws) :: NOT (A AND B) = (NOT A) OR (NOT B) || NOT (A OR B) = (NOT A) AND (NOT B)

# not, or, and, xor

print("=====NOT=====") 
a = False
b = not a
print('data a = ', a)
print('data b = ', b)


print("=====OR=====") 
#jika salah satu true maka hasilnya true #sama dengan penjumlahan false = 0 & true =1 
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

print("=====AND=====") 
#jika dua'nya true hasilnya true selebihnya false #sama dengan perkalian true = 1 false = 0  
a = False
b = False
c = a ^ b
print(a,'AND',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'AND',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'AND',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'AND',b,'=',c)

print("=====XOR=====") 
#akan true jika salah satu true, sisanya false  
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)


                                                                        ###latihan komparasi dan logika### EPS.12
#membuat area gabungan yang berbeda
print('''
LATIHAN KOMPARASI LOGIKA
''')
#++++++++++3-------------10++++++++++++
inputuser = float(input('masukan angka kurang dari 3 dan lebih dari 10 :'))

#++++++++++3-------------
#memeriksa nilai kurang dari 3
print('''  ==========kurang dari========== ''')
iskurangdari = (inputuser < 3) 
print("hasil operasi kurang dari : ", iskurangdari)




#------------10++++++++++
#memeriksa nilai lebih dari 10
print('''  ==========lebih dari==========  ''')
islebihdari = (inputuser > 10)
print("hasil operasi lebih dari : ", islebihdari)


#++++++++++3-------------10++++++++++
#dengan keyword OR
iscorrect = iskurangdari or islebihdari
print("nilai angka yang dimasukan : ", iscorrect)

#----------3++++++++++10----------
print('''
KASUS IRISAN
''')
#kasus irisan
inputuser = float(input('masukan angka lebih dari 3 dan kurang dari 10 :'))


#---------3++++++++++
# lebih dari 3
islebihdari = inputuser > 3 
print("lebih dari : ", islebihdari)


#++++++++++10----------
# kurang dari 10
iskurangdari = inputuser < 10 
print("kurang dari : ", iskurangdari)


#----------3++++++++++10----------
#dengan keyword AND
iscorrect = iskurangdari and islebihdari
print("nilai angka yang dimasukan : ", iscorrect)


# LATIHAN MANDIRI

# SOAL 1 : ----0++++5----8++++11----
# SOAL 2 : ++++0----5++++8----11++++


# SOAL 1
inputuser = float(input("masukkan angka sesuai rules :"))
rules1 = inputuser > 0
rules2 = inputuser < 5
rules3 = inputuser > 8
rules4 = inputuser < 11

jawaban1 = rules1 and rules2 or rules3 and rules4
print("jawabannya adalah :", jawaban1)

# SOAL 2
inputuser = float(input("masukkan angka sesuai rules :"))
rules1 = inputuser < 0
rules2 = inputuser > 5
rules3 = inputuser < 8
rules4 = inputuser > 11

jawaban2 = rules1 or rules2 and rules3 or rules4
print("jawabannya adalah :", jawaban2)


                                                                                   ###operator bitwise### EPS.13
# operator bitwise, operasi biner, binary
print(" === BITWISE OPERATION ===")
a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n========OR=========')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('------------------------(|)')
print('nilai :',c,',binary :',format(c,'08b'))


# bitwise AND (&)
c = a & b
print('\n========AND=========')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('------------------------(&)')
print('nilai :',c,',binary :',format(c,'08b'))


# bitwise XOR (^)
c = a & b
print('\n========XOR=========')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('------------------------(^)')
print('nilai :',c,',binary :',format(c,'08b'))


# bitwise NOT (~)
c = ~a
print('\n========NOT=========')
print('nilai :',a,',binary :',format(a,'08b'))
print('------------------------(~)')
print('nilai :',c,',binary :',format(c,'08b'))
print('------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai ',e^d,',binary :',format(e^d,'08b'))

# shifting (>>/<<)
c = a >>2
print("===== shifting right =====")
print('nilai :',a,',binary :',format(a,'08b'))
print('------------------------(>>)')
print('nilai :',c,',binary :',format(c,'08b'))


print("===== shifting left =====")
c = a <<2
print('nilai :',a,',binary :',format(a,'08b'))
print('------------------------(<<)')
print('nilai :',c,',binary :',format(c,'08b'))

