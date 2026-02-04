#match digunakan untuk melakukan tindakan berbeda berdasarkan kondisi yang berbeda.
#Daripada menulis banyak if..else pernyataan, Anda bisa menggunakan match
#Salah satu dari banyak blok kode yang akan dieksekusi

day = 4 ## Mencocokkan nilai variabel day dengan beberapa kemungkinan kasus
match day:
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')

'''Nilai Default
Gunakan karakter garis bawah _ sebagai
nilai kasus terakhir jika Anda ingin blok
kode dieksekusi ketika tidak ada kecocokan lain'''

day = 4
match day:
    case 5:
        print('jumat')
    case 6:
        print('sabtu')
    case 7:
        print('minggu')
    case _:
        print('tidak ada hari') #Nilai _ akan selalu cocok, jadi penting untuk menempatkannya sebagai kasus terakhir agar berfungsi sebagai kasus default

#Gunakan karakter pipa | sebagai operator "atau" dalam evaluasi kasus untuk memeriksa kecocokan lebih dari satu nilai dalam satu kasus

day = 4
match day: ## Mencocokkan nilai variabel day
    case 1| 2| 3| 4| 5:
     print('hari ini sibuk') #  Jika day bernilai 1, 2, 3, 4, atau 5 maka jalankan ini
    case 6| 7:
     print('aku cinta hari libur')#  Jika day bernilai 6,7 maka jalankan ini

#menambahkan ifpernyataan dalam evaluasi kasus sebagai pengecekan kondisi tambahan
month = 5 # Mencocokkan nilai variabel day
day = 4
match day:
    # Jika day adalah 1–5 DAN month bernilai 4 maka jalankan case ini
    case 1| 2| 3| 4| 5 if month == 4:
        print('hari sibuk bukan april')
    ## Jika day adalah 1–5 DAN month bernilai 5 maka jalankan case ini
    case 1| 2| 3| 4| 5 if month == 5:
        print('hari sibuk bulan mei')
    # Jika tidak ada kondisi yang cocok
    case _:
        print('hari libur')