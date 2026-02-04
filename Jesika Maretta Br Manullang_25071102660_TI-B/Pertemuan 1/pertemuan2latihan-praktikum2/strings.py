#A)python strings
#1)menampilkan literal string dengan print()
print("jeyu")

#2)menggunakan tanda kutip di dalam sebuah string
print("jeyu menulis buku 'jejak jejak waktu'")

#3)Memberikan nilai string ke sebuah variabel
a = "galaksi"
print(a)

#4)menetapkan string multi-baris ke variabel dengan menggunakan tiga tanda kutip
a = """ jesika adalah
seorang presiden
di negeri tetangga"""
print(a)

#5)Tanda kurung siku dapat digunakan untuk mengakses elemen-elemen dalam string.
b = 'jeyu'
print(b[1])

#6) melakukan perulangan melalui karakter-karakter dalam string menggunakan sebuah forloop.
for x in 'jeyu':
  print(x)

#7)mendapatkan panjang sebuah string, gunakan len()
a = "jejes"
print(len(a))

#8)memeriksa apakah frasa atau karakter tertentu ada dalam sebuah string
a = 'lingkupilah pikiranmu dengan obat'
print('pikiranmu' in a)

a = 'lingkupi pikiranmu dengan obat'
if "pikiranmu" in a:
  print("iya 'pikiranmu' ada")

#9)memeriksa apakah frasa atau karakter tertentu TIDAK ada dalam sebuah string
a = 'lingkupi pikiranmu dengan obat'
print('jika' not in a)

a = 'lingkupi pikiranmu dengan obat'
if 'jika' not in a:
  print("tidak ada 'jika' dalam text ")

  #B)Slicing strings

  #slicing (mengembalikan rentang karakter dengan menggunakan sintaks slice.)
  #  a = 'jeyu pro player em el'
  print(a[4:10]) #Dapatkan karakter dari posisi 4 hingga posisi 10(tidak termasuk) dihitung termasuk spasi

  # slice from the start(Dengan menghilangkan indeks awal, rentang akan dimulai dari karakter pertama)
  a = 'kamu keren'
  print(a[:5]) #Pindahkan karakter dari posisi awal ke posisi 5 (tidak termasuk)

  #slice to the end (Dengan menghilangkan indeks akhir , rentang akan berlanjut hingga akhir)
a = 'semua pasti bisa kamu lalui'
print(a[3:]) #Ambil karakter dari indeks ke 3, dan terus sampai ke akhir

#negative indexing (Gunakan indeks negatif untuk memulai pemotongan dari akhir string)
a = 'bahagia selalu'
print(a[-7:-3])

#C)MODIFY STRINGS
#upper case (mengembalikan string dalam huruf besar)
a = 'jeyu keren'
print(a.upper())

#lower case (mengembalikan string ke dalam huruf kecil)
a = 'JEYU KEREN'
print(a.lower())
#Remove Whitespace(menghapus spasi kosong dari awal atau akhir)
a = ' JEYU KEREN '
print(a.strip())

#replace string (mengganti sebuah string dengan string lain)
a = 'jeyu keren'
print(a.replace ("j", 'k'))
#split string(membagi string menjadi substring jika menemukan kemunculan pemisah)
a = 'jeyu keren'
print(a.split(",")) # returns [jeyu keren']
#D)concatenate string (Untuk menggabungkan dua string, Anda dapat menggunakan operator +)
a = 'kamu' #Gabungkan variabel a dengan variabel b ke dalam variabel c
b = 'hebat'
c = a + b
print(c)

a ='kamu'
b ='hebat'
c = a + " " + b
print(c)

#E)string format
#F-string (menggabungkan string dan angka dengan menggunakan f-string)
umur = 20
a = f"nama saya jeyyu,umur saya {umur}"
print(a)

#Placeholders(Placeholder dapat berisi variabel, operasi, fungsi, dan pengubah untuk memformat nilai)
harga = 50
a = f"baju itu jeyu beli dengan harga {harga} rupiah"
print(a)
#modifier(Placeholder dapat menyertakan modifier untuk memformat nilai tersebut.Sebuah pengubah disertakan dengan menambahkan titik dua :diikuti oleh jenis format yang sah)
harga = 50
a = f'baju itu jeyyu beli dengan harga {harga:.2f} rupiah' #Tampilkan harga dengan 2 angka desimal
print(a)
#Placeholder dapat berisi kode Python, seperti operasi matematika
harga = f"baju itu jeyu beli dengan harga {10*2} rupiah"
print(harga)

"""F)Escape Characters(Untuk menyisipkan karakter yang tidak
 sah dalam sebuah string, gunakan karakter escape.
Karakter escape adalah garis miring terbalik \)"""

A = "suara deru angin membuat ku merasa \"tenang\" seperti dulu"
print(A)

#	Single Quote
a = 'it\'s so bad'
print(a)

#Backslash
a = 'kamu mencintai aku \\ dia'
print (a)

#New Line
a = " jeyu\nkeren"
print(a)

#Carriage Return
a = "aku\rdia"
print(a)

#Tab
a = "kamu\tdia"
print(a)

#Backspace
a = 'kamu\bdia'
print(a)

#Octal value
txt = "\110\145\154\154\157"
print(txt)

#	Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
