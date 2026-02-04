#Dengan perulangan while, kita dapat mengeksekusi serangkaian pernyataan selama suatu kondisi bernilai benar.
#Cetak i selama i kurang dari 6

i = 6
while i < 8: # Selama nilai i masih kurang dari 8
 print(i) # Menampilkan nilai i
 i += 6 # # Menambahkan 6 ke nilai i setiap perulangan

#ingat untuk menambah nilai i, jika tidak, perulangan akan terus berjalan selamanya
'''Alur eksekusi:
i = 6
Cek kondisi i < 8 → True
Cetak 6
i += 6 → i menjadi 12
Cek lagi i < 8 → False
Perulangan berhenti'''


#Dengan pernyataan break , kita dapat menghentikan perulangan meskipun kondisi while bernilai benar
#Keluar dari loop ketika i adalah 3
i = 3
while i < 6: # Selama nilai i masih kurang dari 6
 print(i)  # Menampilkan nilai i
 if i == 3:  # Jika i bernilai 3, hentikan perulangan
   break
 i += 1 #menambah nilai i +1 setiap perulangan

 #Dengan pernyataan continue, kita dapat menghentikan iterasi saat ini, dan melanjutkan ke iterasi berikutnya
 #Lanjutkan ke iterasi berikutnya jika i adalah 3
i = 0
# Selama nilai i masih kurang dari 6
while i < 6:
  i += 1 ## Menambahkan 1 ke nilai i setiap perulangan
  if i == 3:# Jika i bernilai 3, lewati perulangan ini
   continue # Lompat ke iterasi berikutnya (print tidak dijalankan)
  print(i) ## Menampilkan nilai i selain 3

#Dengan pernyataan else , kita dapat menjalankan blok kode sekali saja ketika kondisi tersebut tidak lagi benar
i =6
# Selama i masih kurang dari 6
while i < 6:
 print(i)
 i += 1
 # Bagian else dijalankan jika while selesai TANPA break
else:
 print('i is no  longer less than 6')
