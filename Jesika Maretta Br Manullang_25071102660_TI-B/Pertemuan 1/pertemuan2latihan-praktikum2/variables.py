#A)python variables
#1)Membuat variabel
x = 5
y = "Jesika"
print(x)
print(y)
#2)menentukan tipe data suatu variabel
a = str(3)
b = int(3)
c = float(3)

print(a)
print(b)
print(c)

e = "kasih"
print(type(e))

"""
3)Variabel tidak perlu dideklarasikan dengan tipe tertentu ,
 dan bahkan dapat mengubah tipenya setelah ditetapkan.

"""
z = 6
z = "Maretta"
print(z)

#Nama variabel peka terhadap huruf besar dan kecil.
R = 4
r = 'jes'
print(R)
print(r)

#B)variable mames
#1)Legal variable names
myvar = "Jeyu"
my_var = "Jeyu"
_my_var = "Jeyu"
myVar = "Jeyu"
MYVAR = "Jeyu"
myvar2 = "Jeyu"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Nama variabel yang terdiri dari lebih dari satu kata dapat sulit dibaca
#Pascal Case
CalonEngineer = 'Jejes'
print(CalonEngineer)
#Camel Case
calonengineer = 'Jejes'
print(calonengineer)
#Snake Case
calon_engineer = 'Jejes'
print(calon_engineer)

#C)Assign Multiple Values 
#1)Satu Nilai untuk Beberapa Variabel
j,k,l = "Jangan", "Pernah", "Menyerah"
print(j)
print(k)
print(l)

#2)Mengekstrak Array ke dalam variabel
Rumah = ["Bapak", "Ibu", "Saudara"]
A , B  , C = Rumah
print(A)
print(B)
print(C)

#D)Ouput Varibles
#1)Fungsi  print() sering digunakan untuk menampilkan variabel.
X = 'Waktu Menelan Semuanya Perlahan'
print(X)

#2)menampilkan beberapa variabel, dipisahkan oleh koma
X = "Waktu"
Y = "Menelan"
Z = "Semuanya Perlahan"
print(X,Y,Z)

#3)menggunakan + operator untuk menampilkan beberapa variabel 
x = "Lilin-Lilin "
y = "itu ternyata "
z = "mulai padam tapi tak ingin"
print(x + y + z)

#4) Untuk angka, + karakter tersebut berfungsi sebagai operator matematika
x = 5
y = 20 
print(x+y)

#5 untuk menampilkan beberapa variabel dalam print()fungsi adalah dengan memisahkannya menggunakan koma
x = 1
y = 'jeyu'
print(x,y)

#D Global Variables (Variabel global dapat digunakan oleh siapa saja, baik di dalam fungsi maupun di luar fungsi
#1) variabel di luar fungsi, dan gunakan variabel tersebut di dalam fungsi
x = ' bahagia selalu '
def myfunc():
    print('kamu harus' + x)

myfunc()

#2 variabel di dalam fungsi, dengan nama yang sama dengan variabel global
x = ' bahagia selalu'
def myfunc():
   x = ' sehat selalu' 
   print('kamu harus ' + x)
myfunc()
print('kamu harus' + x)

#3 membuat variabel global di dalam sebuah fungsi, Anda dapat menggunakan globalkata kunci `var`
def myfunc():
    global x
    x = 'engineer sejati'
myfunc()
print('jeyu ' + x)

 #4 gunakan globalkata kunci jika Anda ingin mengubah variabel global di dalam sebuah fungsi
x = 'sejauh apa pun'
def myfunc():
   global x
   x = 'beribu langlah kamu berjalan '
myfunc()
print(x +'rumah adalah tempat ternyaman')
