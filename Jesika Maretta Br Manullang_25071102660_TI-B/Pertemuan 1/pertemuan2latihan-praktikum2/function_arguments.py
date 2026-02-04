#Informasi dapat diteruskan ke fungsi sebagai argumen.
#Argumen ditentukan setelah nama fungsi, di dalam tanda kurung. Anda dapat menambahkan argumen sebanyak yang Anda inginkan, cukup pisahkan dengan koma.
#Contoh berikut memiliki fungsi dengan satu argumen (fname). Saat fungsi dipanggil, kita meneruskan nama depan, yang digunakan di dalam fungsi untuk mencetak nama lengkap

#Sebuah fungsi dengan satu argumen
def myFunction (fname): # Mendefinisikan fungsi bernama myFunction dengan parameter fname
    print(fname + ' refsnes')  # Cetak nilai fname ditambah string ' refsnes'

myFunction('emil')# Panggil fungsi dengan fname = 'emil'
myFunction('tobias')# Panggil fungsi dengan fname = 'tobias'
myFunction('linus') # Panggil fungsi dengan fname = 'linus'

#Istilah parameter dan argumen dapat digunakan untuk hal yang sama: informasi yang diteruskan ke suatu fungsi.
#Parameter adalah variabel yang tercantum di dalam tanda kurung pada definisi fungsi
#Argumen adalah nilai sebenarnya yang dikirim ke fungsi saat fungsi tersebut dipanggil
def my_function(name):   # name adalah parameter fungsi
    print("Hello", name) # Cetak "Hello" diikuti nilai parameter

my_function("Emil")      # "Emil" adalah argument yang dikirim ke fungsi

#Secara default, sebuah fungsi harus dipanggil dengan jumlah argumen yang tepat
#Jika fungsi Anda mengharapkan 2 argumen, Anda harus memanggilnya dengan tepat 2 argumen
#Fungsi ini mengharapkan 2 argumen, dan menerima 2 argumen::
def my_function(fname, lname):      # Fungsi dengan 2 parameter: fname dan lname
    print(fname + " " + lname)      # Gabungkan fname dan lname dengan spasi di tengah

my_function("Emil", "Refsnes")      # Memanggil fungsi dengan argument Emil dan Refsnes

#Anda dapat menetapkan nilai default untuk parameter. Jika fungsi dipanggil tanpa argumen, fungsi tersebut akan menggunakan nilai default
def my_function(name="friend"):  # Parameter 'name' punya nilai default "friend"
    print("Hello", name)

my_function("Emil")   # Mengirim argument "Emil"
my_function("Tobias") # Mengirim argument "Tobias"
my_function()         # Tidak mengirim argument → pakai default "friend"
my_function("Linus")  # Mengirim argument "Linus"

#Nilai default untuk parameter country
def my_function(country="Norway"):  # Parameter 'country' punya nilai default "Norway"
    print("I am from", country)     # Cetak negara

my_function("Sweden")  # Kirim argument → country = "Sweden"
my_function("India")   # Kirim argument → country = "India"
my_function()          # Tidak kirim argument → pakai default "Norway"
my_function("Brazil")  # Kirim argument → country = "Brazil"

#Anda dapat mengirim argumen dengan sintaks key = value .
def my_function(animal, name):              # Fungsi dengan dua parameter: animal dan name
    print("I have a", animal)               # Cetak jenis hewan
    print("My", animal + "'s name is", name) # Cetak nama hewan

my_function(animal="dog", name="Buddy")    # Memanggil fungsi menggunakan keyword arguments


#Saat Anda memanggil fungsi dengan argumen tanpa menggunakan kata kunci, argumen tersebut disebut argumen posisional.
#Argumen posisional harus berada dalam urutan yang benar:
def my_function(animal, name):              # Fungsi dengan dua parameter: animal dan name
    print("I have a", animal)               # Cetak jenis hewan
    print("My", animal + "'s name is", name) # Cetak nama hewan

my_function("dog", "Buddy")                # Memanggil fungsi menggunakan positional arguments

#Urutan itu penting dalam argumen posisional
#Mengubah urutan akan mengubah hasilnya
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("Buddy", "dog")  # Argument pertama = "Buddy", kedua = "dog"


#Anda dapat mengirimkan tipe data apa pun sebagai argumen ke suatu fungsi (string, angka, daftar, kamus, dll.).
#Tipe data akan dipertahankan di dalam fungsi:
#Mengirim daftar sebagai argumen
def my_function(fruits):      # Fungsi dengan satu parameter: fruits
    for fruit in fruits:      # Loop untuk setiap item di dalam fruits
        print(fruit)          # Cetak item (fruit) saat ini

my_fruits = ["apple", "banana", "cherry"]  # List yang berisi buah
my_function(my_fruits)                      # Memanggil fungsi dan mengirim list

#Mengirimkan kamus sebagai argumen
def my_function(person):          # Fungsi dengan parameter 'person'
    print("Name:", person["name"]) # Ambil value dari key "name"
    print("Age:", person["age"])   # Ambil value dari key "age"

my_person = {"name": "Emil", "age": 25}  # Dictionary yang berisi informasi
my_function(my_person)                    # Memanggil fungsi dengan dictionary


#Fungsi dapat mengembalikan nilai menggunakan returnpernyataan
def my_function(x, y):    # Fungsi dengan dua parameter: x dan y
    return x + y          # Mengembalikan hasil penjumlahan x + y

result = my_function(5, 3)  # Memanggil fungsi, hasilnya disimpan di variabel 'result'
print(result)               # Mencetak hasil

#Fungsi dapat mengembalikan tipe data apa pun, termasuk daftar, tuple, kamus, dan banyak lagi
#Fungsi yang mengembalikan sebuah daftar:
def my_function():                # Fungsi tanpa parameter
    return ["apple", "banana", "cherry"]  # Mengembalikan sebuah list

fruits = my_function()            # Memanggil fungsi dan menyimpan list di variabel 'fruits'
print(fruits[0])                  # Cetak item pertama di list → "apple"
print(fruits[1])                  # Cetak item kedua di list → "banana"
print(fruits[2])                  # Cetak item ketiga di list → "cherry"

#Fungsi yang mengembalikan tuple
def my_function():  
    return (10, 20)   # Fungsi mengembalikan tuple (10, 20)

x, y = my_function()  # Unpacking tuple → x = 10, y = 20
print("x:", x)        # Cetak x
print("y:", y)        # Cetak y

#Anda dapat menentukan bahwa suatu fungsi HANYA dapat memiliki argumen posisional
#Untuk menentukan argumen hanya berdasarkan posisi, tambahkan , /setelah argumen
def my_function(name, /):  # '/' artinya semua parameter sebelum '/' hanya bisa diisi secara positional
    print("Hello", name)

my_function("Emil")        # Memanggil fungsi dengan argument positional

#Dengan , /, Anda akan mendapatkan kesalahan jika mencoba menggunakan argumen kata kunci:
def my_function(name, /):  # '/' artinya parameter sebelum '/' **hanya bisa diisi secara positional**
    print("Hello", name)

my_function(name="Emil")   # Mencoba mengisi parameter dengan keyword

#Tanpa *,, Anda diperbolehkan menggunakan argumen posisi meskipun fungsi tersebut mengharapkan argumen kata kunci:
def my_function(*, name):  # '*' artinya semua parameter setelah '*' **harus diisi dengan keyword**
    print("Hello", name)

my_function("Emil")        # Mencoba mengisi parameter tanpa keyword

#Anda dapat menggabungkan kedua tipe argumen dalam fungsi yang sama
#Argumen sebelum /hanya berupa argumen posisional, dan argumen setelah *hanya berupa argumen kata kunci:
def my_function(a, b, /, *, c, d):  # a, b → positional-only, c, d → keyword-only
    return a + b + c + d             # Mengembalikan hasil penjumlahan

result = my_function(5, 10, c=15, d=20)  # Memanggil fungsi
print(result)
                             # Mencetak hasil
