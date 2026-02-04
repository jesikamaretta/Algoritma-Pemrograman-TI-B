#Array digunakan untuk menyimpan beberapa nilai dalam satu variabel tunggal
cars = ["Ford", "Volvo", "BMW"]
print(cars[0])

x = len(cars) #returnnya pasti integer
print(x)
 #jumlah total suatu array

#Anda dapat menggunakan for inperulangan untuk menelusuri semua elemen dalam sebuah array.
  #cetak setiap item dalam carsarray:
for x in cars: #(returnnya itu value )
 print(x)

#Tambahkan satu elemen lagi ke dalam carsarray:

cars.append("Honda")
print(cars)

cars.pop(1) #menampilkan apa yg dihilangkan
print(cars)
cars.remove("Volvo") #langsung menghapus
print(cars)

#Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))