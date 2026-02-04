#int (Int, atau integer, adalah bilangan bulat, positif atau negatif, tanpa desimal, dengan panjang tak terbatas)
x = 20
y = 1111
z = -20
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#float ( adalah bilangan, positif atau negatif, yang mengandung satu atau lebih angka desima)
a = 20.0
b = 1111.0
c =-20.0
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#complex (Bilangan kompleks ditulis dengan huruf "j" sebagai bagian imajiner)
x = 3+5j
y = 2j
z = -2j
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#type conversion (mengkonversi dari satu tipe ke tipe lain dengan metode int(), float(), dan complex() )
x = 8 #int
y = 9.0 #float
z = 6j #complex

#convert int menjadi float
X = float(x)
#convert float menjadi complex
Y = complex(y)
#convert complex menjadi int
Z = int(z.real)
print(X)
print(type(X))
print(Y)
print(type(Y))
print(Z)
print(type(Z))
