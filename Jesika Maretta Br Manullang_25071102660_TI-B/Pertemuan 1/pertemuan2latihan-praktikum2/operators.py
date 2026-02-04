#B)Python Operators(Operator digunakan untuk melakukan operasi pada variabel dan nilai)
print(10 + 1) #menggunakan + operator untuk menjumlahkan dua nilai
sum1 = 100
sum2 = sum1 + 20
sum3 = sum2 + sum1
print(sum1)
print(sum2)
print(sum3)

#B)Arithmetic Operators
x = 80
y = 6

print(x+y) #penjumlahn
print(x-y) #pengurangan
print(x*y) #perkalian
print(x/y) #pembagian selalu menghasilkan float
print(x%y) #sisa bagi
print(x**y) #eksponen ,80 pangkat 6
print(x//y) #membagi 2 angka kemudian dibulatkan ke bawah

#C)Assignment Operators(digunakan untuk menetapkan nilai ke variabel)
x = 5
print(x)#Assignment dasar

x = 2
x += 3
print(x) #penjumlahan sama dengan x = x + 3

x = 6
x -= 3
print(x)#pengurangan,sama dengan x = x - 3

x = 2
x *= 3
print(x)#perkalian ,sama dengan x = 2 x 3

x = 6
x /= 3
print(x)#pembagian,sama dengan x=6:3

x = 10
x %= 4
print(x) #modulus,sisa bagi,sama dengan x =10%4

x = 10
x //= 4
print(x)#floor division yaitu hasil bagi yang dibulatkan ke bawah,sama dengan x=10//4
 
x = 5
x **= 2
print(x) #eksponen,sama dengan x=5**2

x = 4
x &= 2 #AND Bit akan bernilai 1 hanya jika dua-duanya sama.
print(x) #Bitwise Assignment (level lanjut) Dipakai di operasi bit biner

x = 4
x |= 2 #OR | Bit bernilai 1 jika salah satu bernilai sama.
print(x)

x = 2
x ^= 2
print(x) #Bit bernilai 1 jika berbeda.

x = 3
x >>= 2 #Shift kanan
print(x)

x = 3
x <<= 2 #shift kiri
print(x)

print(x:=2)#walrus operator ,sama dengan x=3 print(x)

#The Walrus Operator
numbers= [1,2,3,4,5]
if (count := len(numbers)) > 3:
    print(f'lis has {count} elements') #menghitung elemen numbers

#D)Comparison Operators   
x = 4
y = 2
print(x==y) # mencetak true jika x sama dengan y dan false jika sebaliknya
print(x<y) # mencetak true jika x kecil dari y dan false jika sebaliknya
print(x>y) # mencetak true jika x besar dari y dan false jika sebaliknya
print(x<=y)# mencetak true jika x kecil dari atau sama dengan y dan false jika tidak
print(x>=y)# mencetak true jika x besar dari atau sama dengan y dan false jika tidak
print(x!=y)# mencetak true jika x tidak sama denan y dan false jika sebaliknya

#Chaining Comparison Operators(menggabungkan operator perbandingan)
x = 4
print(1>x>5) # mencetak true jika c kecil dari 1 dan besar dari 5
print(1<x and x<5) #mencetak true jika x lebih besar dari 1 DAN x lebih kecil dari 5

#E)Logical Operators(Operator logika digunakan untuk menggabungkan pernyataan bersyarat)
x = 2
print(x>1 and x<10)#mencetak true karena keduanya benar ,and → semua harus benar

x = 4
print(x>6 or x<10)#mencetak true karena salah satu benar,or → salah satu benar

x = 6
print(not 10<x and x<8) #mencetak true karena tidak memenuhi kedua keadaan,not → keduanya salah

x =['jeyu', 'arin', 'gledis']
y =['jeyu', 'arin', 'gledis']
print(x is y)
print(y is x)
print(x == y) #Operator isakan mengembalikan nilai Truejika kedua variabel menunjuk ke objek yang sama

x =['elsa', 'okta', 'ade']
y =['jeyu', 'arin', 'gledis']
print(x is not y)#Operator is notakan mengembalikan nilai Truejika kedua variabel tidak menunjuk ke objek yang sama

x =[1,2,3]
y =[1,2,3]
print(x is y)#is - Memeriksa apakah kedua variabel menunjuk ke objek yang sama di memori.

print(x == y)#== - Memeriksa apakah nilai kedua variabel sama

#F)Membership Operators( digunakan untuk menguji apakah suatu urutan terdapat dalam suatu objek)

TIB =['jejes', 'gledis', 'arin']
print('anas' in TIB) #in memeriksa apakah string "anas" ada pada array TIB,mencetak false karena anas tidak ada di array TIB

TIB =['jejes', 'arin', 'gledis']
print('anas' not in TIB) #memeriksa bahwa anas tidak ada pada array TIB dan mencetak true apabila benar anas tidak ada di array TIB

a = 'jeyu keren'
print('j' in a) #dengan in mencetak true kare 'j' ada di dalam string a
print('keren' in a) # dengan in mencetak true karena 'keren' ada di string a
print('o' not in a)#dengan not in mencetak true karena 'o' tidak ada di string a

#G)Bitwise Operators(Operator bitwise digunakan untuk membandingkan angka (biner))
#Operator & membandingkan setiap bit dan menetapkannya menjadi 1 jika keduanya bernilai 1, jika tidak, nilainya ditetapkan menjadi 0
print(6 & 3)
"""Representasi biner dari 6 adalah 0110.
Representasi biner dari 3 adalah 0011.
Kemudian operator & membandingkan bit-bit tersebut
 dan mengembalikan 0010,
 yang setara dengan 2 dalam desimal """

#Operator | membandingkan setiap bit dan menetapkannya menjadi 1 jika salah satu atau kedua bit bernilai 1, jika tidak, nilainya ditetapkan menjadi 0
print(6|3)
 # 6 = 0110
# 3 = 0011
# --------
# 7 = 0111

#Operator ^ membandingkan setiap bit dan menetapkannya menjadi 1 jika hanya satu yang bernilai 1, jika tidak (jika keduanya bernilai 1 atau keduanya bernilai 0) maka nilainya ditetapkan menjadi 0
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

print(6 ^ 3)

#Operator Precedence
#dimulai dengan prioritas tertinggi
#1Parentheses(Tanda kurung)
print((6+3) - (6+3))
"""
Tanda kurung memiliki prioritas tertinggi dan harus dihitung terlebih dahulu.
Perhitungan di atas menjadi 9 - 9 = 0.
"""

#2 eksponen
print(100 - 3 ** 3)

"""
Operator perpangkatan memiliki prioritas lebih tinggi daripada pengurangan,
sehingga harus dihitung terlebih dahulu.
Perhitungan di atas menjadi 100 - 27 = 73.
"""

#3 Operator bitwise NOT,Unary plus, unary minus
print(100 + ~3)
"""
Operator bitwise NOT memiliki prioritas lebih tinggi daripada penjumlahan,
sehingga dihitung terlebih dahulu.
Perhitungan di atas menjadi 100 + (-4) = 96.
"""

#4 Multiplication, division, floor division, and modulus
print(100 + 5 * 3)
"""
Operator perkalian memiliki prioritas lebih tinggi daripada penjumlahan,
sehingga dihitung terlebih dahulu.
Perhitungan di atas menjadi 100 + 15 = 115.
"""

#5 Addition and subtraction
print(100 - 5 * 3)
"""
Operator pengurangan memiliki prioritas lebih rendah daripada perkalian,
sehingga perkalian harus dihitung terlebih dahulu.
Perhitungan di atas menjadi 100 - 15 = 85.
"""
#6 Bitwise left dan right shift (pergeseran bit ke kiri dan ke kanan)
print(8 >> 4 - 2)
#8  = 0000000000001000
#>> 2
#2  = 0000000000000010

#7 	Bitwise AND
print(6 & 2 + 1)

"""
Operator penjumlahan (+) memiliki prioritas lebih tinggi daripada operator bitwise AND (&),
sehingga penjumlahan harus dihitung terlebih dahulu.

Perhitungannya menjadi:
2 + 1 = 3
6 & 3 = 2

Penjelasan bitwise AND (&):
Operator & membandingkan setiap bit.
Jika kedua bit bernilai 1, maka hasilnya 1.
Jika salah satu atau keduanya bernilai 0, maka hasilnya 0.

Representasi biner:
6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
"""

#8 Bitwise XOR
print(6 ^ 2 + 1)

"""
Operator penjumlahan (+) memiliki prioritas lebih tinggi daripada operator bitwise XOR (^),
sehingga penjumlahan harus dihitung terlebih dahulu.

Perhitungannya menjadi:
2 + 1 = 3
6 ^ 3 = 5

Penjelasan bitwise XOR (^):
Operator ^ membandingkan setiap bit.
Jika hanya salah satu bit bernilai 1, maka hasilnya 1.
Jika kedua bit sama (keduanya 1 atau keduanya 0), maka hasilnya 0.

Representasi biner:
6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
"""

#9	Bitwise OR
print(6 | 2 + 1)

"""
Operator penjumlahan (+) memiliki prioritas lebih tinggi daripada operator bitwise OR (|),
sehingga penjumlahan harus dihitung terlebih dahulu.

Perhitungannya menjadi:
2 + 1 = 3
6 | 3 = 7

Penjelasan bitwise OR (|):
Operator | membandingkan setiap bit.
Jika salah satu atau kedua bit bernilai 1, maka hasilnya 1.
Jika kedua bit bernilai 0, maka hasilnya 0.

Representasi biner:
6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
"""

#10 Comparisons, identity, and membership operators(==  !=  >  >=  <  <=  is  is not  in  not in)
print(5 == 4 + 1)

"""
Operator penjumlahan (+) memiliki prioritas lebih tinggi daripada operator perbandingan sama dengan (==),
sehingga penjumlahan harus dihitung terlebih dahulu.

Perhitungannya menjadi:
4 + 1 = 5
5 == 5 = True
"""

#11 Logical NOT
print(not 5 == 5)
"""
Operator perbandingan sama dengan (==) memiliki prioritas lebih tinggi
daripada operator logika NOT (not), sehingga perbandingan dihitung terlebih dahulu.

Perhitungannya menjadi:
5 == 5 = True
not True = False
"""

#12 	AND
print(1 or 2 and 3)

"""
Operator logika AND (and) memiliki prioritas lebih tinggi daripada
operator logika OR (or), sehingga ekspresi AND dihitung terlebih dahulu.

Perhitungannya menjadi:
2 and 3 = 3
1 or 3 = 1
"""

#13 	OR
print(4 or 5 + 10 or 8)

"""
Operator penjumlahan (+) memiliki prioritas lebih tinggi daripada
operator logika OR (or), sehingga penjumlahan dihitung terlebih dahulu.

Perhitungannya menjadi:
5 + 10 = 15
4 or 15 or 8 = 4
"""