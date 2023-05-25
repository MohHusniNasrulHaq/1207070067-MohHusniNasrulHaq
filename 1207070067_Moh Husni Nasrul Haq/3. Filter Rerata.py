import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
#matplotlib inline
import numpy as np #mengimport library numpy untuk array dan matriks
import cv2 #library untuk operasi dalam citra


citra1 = cv2.imread("mobil.jpeg", cv2.IMREAD_GRAYSCALE) #membuka gambar1 dengan opencv dalam pembacaan grayscale

citra2 = cv2.imread("boneka2.jpeg", cv2.IMREAD_GRAYSCALE) #membuka gambar2 dengan opencv dalam pembacaan grayscale

print('Shape citra 1:', citra1.shape) #Mencetak dimensi citra 1
print('Shape citra 2:', citra2.shape)  #Mencetak dimensi citra 2

# Menampilkan kedua citra dalam satu figure menggunakan subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 10)) #membuat subplot dengan ukuran 1x2 dan size 10x10
ax = axes.ravel()  #Meratakan array dari objek subplot

ax[0].imshow(citra1, cmap='gray') #Memunculkan citra pertama
ax[0].set_title("Citra 1") #memberi judul
ax[1].imshow(citra2, cmap='gray') #Memunculkan citra kedua
ax[1].set_title("Citra 2") #memberi judul

copyCitra1 = citra1.copy().astype(float) #membuat copy dan menjadi citra1 kedalam plot-plot dalam hasil output
copyCitra2 = citra2.copy().astype(float) #membuat copy dan menjadi citra2 kedalam plot-plot dalam hasil output

#Mendapatkan dimensi citra1 hasil copy
m1, n1 = copyCitra1.shape #m1 untuk baris dan ni untuk jumlah kolom
output1 = np.empty((m1, n1), dtype=float) #Membuat array kosong dengan ukuran m1 x n1 dan menyimpannya ke dalam variabel output1
#Mendapatkan dimensi citra2 hasil copy
m2, n2 = copyCitra2.shape #m1 untuk baris dan ni untuk jumlah kolom
output2 = np.empty((m2, n2), dtype=float) #Membuat array kosong dengan ukuran m1 x n1 dan menyimpannya ke dalam variabel output2

# Mencetak dimensi copy citra 1 dan output citra 1
print('Shape copy citra 1:', copyCitra1.shape)
print('Shape output citra 1:', output1.shape)
print('m1:', m1) #mencetak nilai baris
print('n1:', n1) #mencetak nilai kolom
print()

# Mencetak dimensi copy citra 2 dan output citra 2
print('Shape copy citra 2:', copyCitra2.shape)
print('Shape output citra 2:', output2.shape)
print('m2:', m2) #mencetak nilai baris
print('n2:', n2) #mencetak nilai kolom
print() 

# Melakukan filter rata-rata pada citra copy pertama
for baris in range(0, m1-1): 
    for kolom in range(0, n1-1):
        a1 = baris # variabel a1 menjadi nilai baris
        b1 = kolom # vriabel b1 menjadi nilai kolom
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1]
        output1[a1, b1] = (1/9 * jumlah)

#Menggunakan filter rata-rata pada citra copy kedua
for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        a1 = baris1
        b1 = kolom1
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1]
        output2[a1, b1] = (1/9 * jumlah)

fig, axes = plt.subplots(2, 2, figsize=(10, 10)) #membuat subplot dengan ukuran matriks 2x2 dan size 10x10
ax = axes.ravel() #Meratakan array dari objek subplot

ax[0].imshow(citra1, cmap='gray') #Memunculkan citra1
ax[0].set_title("Input Citra 1") #memberi judul

ax[1].imshow(citra2, cmap='gray') #Memunculkan citra2
ax[1].set_title("Input Citra 2")#memberi judul

ax[2].imshow(output1, cmap='gray') #Memunculkan citra3
ax[2].set_title("Output Citra 1") #memberi judul

ax[3].imshow(output2, cmap='gray') #Memunculkan citra4
ax[3].set_title("Output Citra 2") #memberi judul

plt.show() #memunculkan seluruh operasi citra 