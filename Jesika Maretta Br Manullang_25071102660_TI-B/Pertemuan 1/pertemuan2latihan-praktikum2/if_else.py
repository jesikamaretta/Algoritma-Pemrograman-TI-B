#A) if
a = 40
b = 30
if a > b:
 print('a lebih besar dari b') #mencetak a lebih besar dari b karena benar 40 lebih besar dari 40

 #Pernyataan if mengevaluasi suatu kondisi (ekspresi yang menghasilkan True atau False ).
 #  Jika kondisinya benar, blok kode di dalam pernyataan if akan dieksekusi.
 #  Jika kondisinya salah, blok kode akan dilewati

 angka = 2
 if angka > 0:
  print('angka adalah bilangan positif') #Memeriksa apakah suatu angka positif

#Beberapa Pernyataan dalam Blok If
age = 10
if age <= 18:
 print('kamu anak anak')
 print('kamu tidak bisa memilih')
 print('kamu belum legal')

#Variabel Boolean dapat digunakan langsung dalam pernyataan if tanpa operator perbandingan
login = True
if login:
 print("selamat datang")

 # Python Elif Statement(Kata kunci elif adalah cara Python untuk mengatakan "jika kondisi sebelumnya tidak benar, maka coba kondisi ini")
a = 33
b = 33
if a > b:
 print('a lebih besar dari b')
elif a == b:
 print('a sama dengan b') #a sama dengan b , jadi kondisi pertama tidak benar, tetapi kondisi elif benar, sehingga kita mencetak ke layar bahwa "a dan b sama

#Python akan memeriksa setiap kondisi secara berurutan dan mengeksekusi kondisi pertama yang bernilai benar
score = 75

if score >= 90:
    print('predikat A')
elif score >= 80:
    print('predikat B')
elif score >= 75: #karena skornya adalah 75, program akan mencetak "Nilai: C" (kondisi pertama yang bernilai benar)
    print('predikat C') 
elif score >= 60:
    print('predikat D')
else:
    print('tidak lulus')
#Hanya kondisi pertama yang benar yang akan dieksekusi. Bahkan jika beberapa kondisi benar, Python akan berhenti setelah mengeksekusi blok yang cocok pertama

#C) Else
'''Pernyataan `else` menyediakan tindakan default
 ketika tidak ada kondisi sebelumnya yang benar.
 Anggap saja sebagai "penangkap semua" untuk skenario
 apa pun yang tidak tercakup oleh pernyataan `if` dan `elif`'''

#Pernyataan else harus berada di akhir. Anda tidak dapat menggunakan elif setelah else
number = 7
if number % 2 == 0:
 print('number adalah bilangan genap')
else:
 print('number adalah bilangan ganjil')


#menggabungkan if , elif , dan else untuk menciptakan struktur pengambilan keputusan yang komprehensif.
temperature = 25

if temperature >=30:
  print('suhu panas')
elif temperature < 30:
  print('suhu hangat')
elif temperature <= 15:
  print('suhu dingin')
else:
  print('suhu tidak diketahui')

'''Pernyataan `else` berfungsi sebagai
cadangan yang akan dieksekusi ketika tidak
ada satu pun kondisi sebelumnya yang benar.
Hal ini membuatnya berguna untuk
penanganan kesalahan, validasi, dan 
penyediaan nilai default'''

#memvalidasi input pengguna
username = "Emil"

# Mengecek apakah panjang username lebih dari 0 (tidak kosong)
if len(username) > 0:
    # Jika username tidak kosong, tampilkan pesan selamat datang
    print(f"Welcome, {username}!")
else:
    # Jika username kosong, tampilkan pesan error
    print("Error: Username tidak boleh kosong")

#Short Hand If
'''Jika Anda hanya memiliki satu pernyataan
untuk dieksekusi, Anda dapat 
meletakkannya pada baris yang sama dengan 
if pernyataan tersebut'''

a = 10
b = 6
if a > b: print('a lebih besar dari b')

#Satu baris if/ else yang mencetak sebuah nilai
a = 4
b = 10
print('A') if a<b else print ('B')

#menggunakan garis tunggal if/ elseuntuk memilih nilai dan menetapkannya ke variabel
a = 10
b =20
bigger = a if a > b else b
print('bigger is', bigger)

#menggabungkan ekspresi kondisional, tetapi usahakan tetap singkat agar mudah dibaca
#Satu baris, tiga hasil
a = 20
b = 20
print(A) if a > b else print('=') if a == b else print(B)

#Operator ternary sangat berguna untuk penugasan sederhana dan pernyataan pengembalian
#Mencari nilai maksimum dari dua bilangan:
x = 15
y = 20
nilai_maksimum = x if x > y else y
print("nilai maksimum adalah", nilai_maksimum)

#Menetapkan nilai default
username = "" 
# Jika username tidak kosong, gunakan username
# Jika username kosong, gunakan "Guest"
display_name = username if username else "guest"
# Menampilkan pesan selamat datang
print('welcome', display_name)

# E)Logical Operators
'''and adalah operator logika, dan digunakan untuk 
menggabungkan pernyataan kondisional.
Kedua kondisi harus benar agar seluruh ekspresi menjadi benar'''

#Periksa apakah alebih besar dari b, DAN apakah c lebih besar dari a
a = 200
b = 33
c = 500

# Mengecek dua kondisi sekaligus menggunakan operator logika AND
# a > b  → mengecek apakah a lebih besar dari b
# c > a  → mengecek apakah c lebih besar dari a
# Jika KEDUA kondisi bernilai True, maka blok if dijalankan
if a > b and c > a:
    print("Kedua kondisi bernilai True")

#or adalah operator logika, dan digunakan untuk menggabungkan pernyataan kondisional. Setidaknya satu kondisi harus benar agar seluruh ekspresi menjadi benar
#Periksa apakah alebih besar dari b, ATAU apakah a lebih besar dari c
a = 200
b = 33
c = 500

# Mengecek dua kondisi sekaligus menggunakan operator logika AND
# a > b  → mengecek apakah a lebih besar dari b
# c > a  → mengecek apakah c lebih besar dari a
# Jika KEDUA kondisi bernilai True, maka blok if dijalankan
if a > b and c > a:
    print("Kedua kondisi bernilai True")

#not adalah operator logika, dan digunakan untuk membalikkan hasil dari pernyataan kondisional
#Periksa apakah a nilainya TIDAK lebih besar dari b

a = 33
b = 200
# Mengecek kondisi a > b
# Operator NOT (not) akan membalik hasil kondisi
# a > b  → False (33 tidak lebih besar dari 200)
# not False → True
if not a > b:
    print("a TIDAK lebih besar dari b")

#menggabungkan beberapa operator logika dalam satu ekspresi. Python mengevaluasi not terlebih dahulu, kemudian and , lalu or
#Menggabungkan and, or, dan not
age = 25
is_student = False
has_discount_code = True

# Aturan prioritas operator logika di Python:
# 1. not
# 2. and
# 3. or
#
# Tanda kurung ( ) akan dievaluasi lebih dulu

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")

#gunakan tanda kurung untuk memperjelas maksud Anda dan mengontrol urutan evaluasi.
#Gunakan tanda kurung untuk kondisi yang kompleks
temperature = 25
is_raining = False
is_weekend = True

# Aturan prioritas operator logika di Python:
# 1. not
# 2. and
# 3. or
#
# Ekspresi dalam tanda kurung ( ) dihitung terlebih dahulu

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")

#Pemeriksaan autentikasi pengguna
username = "Tobias"
password = "secret123"
is_verified = True

# Mengecek beberapa kondisi sekaligus menggunakan operator logika AND
# username → bernilai True jika tidak kosong
# password → bernilai True jika tidak kosong
# is_verified → True jika akun sudah terverifikasi
# Jika SEMUA kondisi bernilai True, maka login berhasil
if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")


#Pengecekan rentang dengan operator logika
score = 85

# Mengecek apakah nilai berada dalam rentang 0 sampai 100
# score >= 0   → nilai tidak kurang dari 0
# score <= 100 → nilai tidak lebih dari 100
# Jika KEDUA kondisi terpenuhi, maka nilai dianggap valid
if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")

#Nested If

#F)Nested If( memiliki ifpernyataan di dalam ifpernyataan)
x = 41

# Mengecek apakah x lebih besar dari 10

if x > 10:
    print("Above ten,")

    # Jika kondisi pertama True, lanjut cek apakah x > 20
    if x > 20:
        print("and also above 20!")
    else:
        # Bagian ini dijalankan jika x > 10 tapi x <= 20
        print("but not above 20.")


#Memeriksa beberapa kondisi dengan penestingan
age = 25
has_license = True

# Mengecek apakah umur sudah memenuhi syarat untuk mengemudi
if age >= 18:
    # Jika umur 18 tahun atau lebih, lanjut cek kepemilikan SIM
    if has_license:
        print("Kamu boleh mengemudi")
    else:
        # Umur cukup, tapi belum punya SIM
        print("Kamu perlu memiliki SIM")
else:
    # Umur belum memenuhi syarat mengemudi
    print("Kamu masih terlalu muda untuk mengemudi")

# membuat struktur bertingkat sedalam yang dibutuhkan, tetapi perlu diingat bahwa terlalu banyak tingkatan dapat membuat kode lebih sulit dibaca
score = 85
attendance = 90
submitted = True

# Mengecek apakah nilai memenuhi syarat kelulusan
score = 85
attendance = 90
submitted = True

# Mengecek apakah nilai memenuhi syarat kelulusan
if score >= 60:
    # Jika nilai lulus, cek persentase kehadiran
    if attendance >= 80:
        # Jika kehadiran cukup, cek apakah tugas sudah dikumpulkan
        if submitted:
            print("Pass with good standing")
        else:
            # Nilai dan kehadiran cukup, tapi tugas belum dikumpulkan
            print("Pass but missing assignment")
    else:
        # Nilai lulus, tetapi kehadiran kurang
        print("Pass but low attendance")
else:
    # Nilai tidak memenuhi syarat kelulusan
    print("Fail")

#Bisa juga ditulis dengan and
temperature = 25
is_sunny = True

# Mengecek apakah suhu lebih dari 20 derajat
# DAN kondisi cuaca sedang cerah
if temperature > 20 and is_sunny:
    # Jika kedua kondisi bernilai True
    print("Perfect beach weather!")

#Validasi login dengan pemeriksaan bertingkat
username = "Emil"
password = "python123"
is_active = True

# Mengecek apakah username tidak kosong
if username:
    # Jika username ada, cek apakah password tidak kosong
    if password:
        # Jika password ada, cek apakah akun aktif
        if is_active:
            print("Login successful")
        else:
            # Username dan password ada, tapi akun tidak aktif
            print("Account is not active")
    else:
        # Username ada, tetapi password kosong
        print("Password required")
else:
    # Username kosong
    print("Username required")

#Perhitungan nilai dengan logika bertingkat
score = 92
extra_credit = 5

# Mengecek apakah nilai masuk kategori A
if score >= 90:
    # Jika nilai A, cek apakah ada nilai tambahan (extra credit)
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
# Jika tidak masuk A, cek apakah masuk kategori B
elif score >= 80:
    print("B grade")
# Jika nilai di bawah 80
else:
    print("C grade or below")

#Pass Statement
#if Pernyataan tidak boleh kosong, tetapi jika karena suatu alasan Anda memiliki ifpernyataan tanpa isi, masukkan isi pass pernyataan tersebut untuk menghindari kesalahan
a = 33
b = 200

# Mengecek apakah nilai b lebih besar dari a
if b > a:
    # pass digunakan sebagai perintah kosong
    # Artinya: tidak melakukan apa-apa meskipun kondisi bernilai True
    # Biasanya dipakai sebagai placeholder untuk kode yang akan ditambahkan nanti
    pass

#pass in Development
#Tempat penampung untuk implementasi di masa mendatang
age = 16

# Mengecek apakah usia kurang dari 18 tahun
if age < 18:
    # pass digunakan sebagai perintah kosong
    # Artinya: belum ada aksi yang dijalankan untuk kondisi ini
    # TODO berarti: nanti akan ditambahkan logika khusus untuk pengguna di bawah umur
    pass
else:
    # Jika usia 18 tahun atau lebih, akses diberikan
    print("Access granted")

#menggunakan `pass` di cabang mana pun dari pernyataan `if-elif-else`

    value = 50

# Mengecek apakah nilai kurang dari 0
if value < 0:
    # Jika nilai negatif
    print("Negative value")
# Mengecek apakah nilai sama dengan 0
elif value == 0:
    # pass digunakan karena tidak ada aksi yang perlu dilakukan
    # Kondisi ini sengaja dibiarkan kosong
    pass  # Kasus nol – tidak perlu tindakan apa pun
else:
    # Jika nilai lebih besar dari 0
    print("Positive value")
#pass` juga umum digunakan dengan perulangan, fungsi, dan kelas.
def calculate_discount(price):
    # pass digunakan sebagai placeholder
    # Artinya: fungsi ini sudah dibuat, tetapi logika diskon belum diimplementasikan
    # TODO menandakan bahwa kode ini akan dilengkapi di kemudian hari
    pass  # TODO: Implementasikan logika diskon nanti

# Fungsi sudah ada, tetapi saat ini belum melakukan apa pun
