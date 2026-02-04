#Perulangan for digunakan untuk mengulang suatu urutan (baik berupa daftar, tuple, kamus, himpunan, atau string).
#Dengan perulangan for, kita dapat mengeksekusi serangkaian pernyataan, satu kali untuk setiap item dalam daftar, tuple, set, dan lain sebagainya
#Cetak setiap buah dalam daftar buah:
buah = ['jeruk', 'manggis', 'apel']
for x in buah:
  print(x)  # Menampilkan satu buah per perulangan

#Melakukan perulangan melalui sebuah string
#Bahkan string pun merupakan objek yang dapat diiterasi, karena berisi urutan karakter
#Lakukan perulangan melalui huruf-huruf dalam kata "pisang"
buah = 'pisang' # Variabel buah berisi string 'pisang'
for x in buah: # Loop for untuk iterasi tiap karakter dalam string
  print(x) # Menampilkan karakter x saat ini

#Dengan pernyataan `break` , kita dapat menghentikan perulangan sebelum selesai memproses semua item
#Keluar dari perulangan ketika x"apel" 
buah = ['nanas', 'apel', 'semangka']
for x in buah:# Looping tiap item dalam list buah
 print(x) # Menampilkan buah saat ini
 if x == 'apel':  # Jika buah adalah 'apel', hentikan perulangan
  break
 
 #Keluar dari perulangan ketika x nilainya "apel", tetapi kali ini perintah break diletakkan sebelum perintah print
buah =['nanas', 'apel', 'semangka']
for x in buah:
  if x == 'apel':
    break
  print(x) #print(x) → hanya mencetak item sebelum 'apel'

  #Dengan pernyataan `continue` , kita dapat menghentikan iterasi loop saat ini dan melanjutkan ke iterasi berikutnya
  #Jangan mencetak apel
buah = ['nanas', 'apel', 'semangka']
for x in buah:
    if x == 'apel':   # Jika buah adalah 'apel', lewati perulangan ini
      continue # Lompat ke item berikutnya tanpa mencetak 'apel'
    print(x)  # Menampilkan buah saat ini

#Untuk menjalankan serangkaian kode dalam jumlah yang ditentukan, kita dapat menggunakan range()fungsi tersebut.
#Fungsi ini range()mengembalikan serangkaian angka, dimulai dari 0 secara default, dan bertambah 1 (secara default), dan berakhir pada angka yang ditentukan

#Menggunakan fungsi range()
for x in range(6):
  print(x) #Perhatikan bahwa range(6)ini bukan nilai 0 hingga 6, tetapi nilai 0 hingga 5

#Menggunakan parameter awal
for x in range (2, 6): ## Looping dengan range dari 2 sampai 5 (6 tidak termasuk)
  print(x)

#Tambahkan angka 3 pada urutan tersebut (nilai default adalah 1)
for x in range (2, 30, 3): #Looping dengan range dari 2 sampai 29, dengan langkah 3
  print(x)

#Kata elsekunci `in` dalam sebuah forperulangan menentukan blok kode yang akan dieksekusi ketika perulangan selesai:
#Cetak semua angka dari 0 hingga 5, dan cetak pesan ketika perulangan telah berakhir
for x in range(6):
  print(x)
else:
  print('akhirnya') #Blok ini else TIDAK akan dieksekusi jika perulangan dihentikan oleh sebuah breakpernyataan

#Hentikan perulangan saat x nilainya 3, dan lihat apa yang terjadi dengan else blok tersebut
for x in range(6): # Loop dari 0 sampai 5
  if x == 3: break #Loop dari 0 sampai 5
  print(x)# Jika ya, hentikan loop secara paksa #Cetak nilai x jika belum mencapai 3
else: 
  print('akhirnya')

#Perulangan bersarang adalah perulangan di dalam perulangan
#"Loop dalam" akan dieksekusi satu kali untuk setiap iterasi dari "loop luar":
warna = ['merah', 'biru', 'ungu']
buah = ['apel', 'jeruk', 'nanas']
for x in warna: # Loop pertama untuk setiap warna
  for y in buah: # Loop kedua untuk setiap buah
    print(x,y)  # Cetak kombinasi warna dan buah

#forLoop tidak boleh kosong, tetapi jika karena suatu alasan Anda memiliki forloop tanpa isi, tambahkan passpernyataan tersebut untuk menghindari kesalahan
for x in [1,2,3]:
  pass