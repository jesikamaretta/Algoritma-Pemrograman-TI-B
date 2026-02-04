#Boolean Values(mengevaluasi ekspresi apa pun di Python, dan mendapatkan salah satu dari dua jawaban, True atau False.)
print(20 < 8)
print(20 == 8)
print(20 > 8)

#Cetak pesan berdasarkan apakah kondisinya benar True atau salah False
a = 20
b = 10

if a > b:
    print('a lebih dari b')
else:
    print('a kurang dari b')

#mengevaluasi nilai apa pun, dan memberikan hasil berupa nilai True atau False sebaliknya
print(bool('jeyu'))   
print(bool(1))

#Evaluasi dua variabel
x = 'kamu'
y = 10
print(bool(x))
print(bool(y))
#semua string adalah True, kecuali string kosona apa pun adalah True, kecuali 0.Semua list, tuple, set, dan dictionary adalah True, kecuali yang kosong
print(bool(12))
print(bool('a, b, c'))
print(bool('jes'))

#tidak banyak nilai yang dievaluasi menjadi False, kecuali nilai kosong, seperti (), [], {}, "", angka 0, dan nilai None
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))
#membuat fungsi yang mengembalikan nilai Boolean
def myFunction() :
    return True
print(myFunction())

#Cetak "YA!" jika fungsi mengembalikan nilai True, jika tidak, cetak "TIDAK!"
def myFunction():
    return True
if myFunction():
    print('YES')
else:
    print('NO')

# fungsi `is_boolean_type`, yang dapat digunakan untuk menentukan apakah suatu objek memiliki tipe data tertentu
x = 'jess'
print(isinstance(x, str)) #Periksa apakah suatu objek merupakan string


