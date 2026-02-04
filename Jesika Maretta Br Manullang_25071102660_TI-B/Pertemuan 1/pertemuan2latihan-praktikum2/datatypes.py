#Mengatur tipe data (Dalam Python, tipe data ditentukan saat Anda memberikan nilai ke sebuah variabel)
tipe1 ='1' #str
tipe2 = 1  #int 
tipe3 = 1.5 #float
tipe4 = True #bool
tipe5 =[1,2,3,4] #list
tipe6 =['jesika',2,3] #list
tipe7 =(1,2,3) #tuple
tipe8 ={
    'nama': 'jesika',
    'kelas' :'TI B',
    'nim' :'25071102660',
    'mahasiswa aktif' :True
} #dict
tipe9 = 1j #complex
tipe10 = range(6) #range
tipe11 = {'jejes', 'gledis', 'arin','bita', 'aini'} #set
tipe12 = frozenset({'jejes', 'gledis', 'arin', 'bita', 'aini'}) #frozenset
tipe13 = b"sugoi" #bytes
tipe14 = bytearray(20) #byteaaray
tipe15 = memoryview(bytes(20)) #memoryview
tipe16 = None #nonetype

print(type(tipe1))
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6))
print(type(tipe7))
print(type(tipe8))
print(type(tipe9))
print(type(tipe10))
print(type(tipe11))
print(type(tipe12))
print(type(tipe13))
print(type(tipe14))
print(type(tipe15))
print(type(tipe16))

#Menetapkan Tipe Data Spesifik
tipe1 = str('1') #str
tipe2 = int(1)#int 
tipe3 = float(1.5)#float
tipe4 = bool(True)#bool
tipe5 = list((1,2,3,4)) #list
tipe6 = list(('jesika',2,3)) #list
tipe7 = tuple((1,2,3)) #tuple
tipe8 = dict(
    nama='jesika',
    kelas='TI B',
    nim='25071102660',
    mahasiswa_aktif=True
)

tipe9 = complex(1j) #complex
tipe10 = range(6) #range
tipe11 = set(('jejes', 'gledis', 'arin','bita', 'aini')) #set
tipe12 = frozenset(('jejes', 'gledis', 'arin', 'bita', 'aini')) #frozenset
tipe13 = bytes("sugoi", 'utf-8') #bytes
tipe14 = bytearray(20) #byteaaray
tipe15 = memoryview(bytes(20)) #memoryview


print(type(tipe1))
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6))
print(type(tipe7))
print(type(tipe8))
print(type(tipe9))
print(type(tipe10))
print(type(tipe11))
print(type(tipe12))
print(type(tipe13))
print(type(tipe14))
print(type(tipe15))
