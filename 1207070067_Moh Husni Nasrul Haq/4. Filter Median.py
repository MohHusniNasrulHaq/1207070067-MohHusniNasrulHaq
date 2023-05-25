import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
import numpy as np #mengimport library numpy untuk array dan matriks
import cv2 #library untuk operasi dalam citra
from skimage import data  # Mengimpor modul data dari skimage untuk mengakses contoh citra
from skimage.io import imread  # Mengimpor fungsi imread dari modul skimage.io untuk membaca citra
from skimage.color import rgb2gray # Mengimpor fungsi rgb2gray dari modul skimage.color untuk mengubah citra menjadi citra grayscale



citra1 = imread(fname = "mobil.jpeg") #membuka gambar1 dengan skimage
citra2 = imread(fname = "boneka2.jpeg") #membuka gambar2 dengan skimage

#mencetak bentuk citra 1 dan 2
print('Shape citra 1 : ', citra1.shape)
print('Shape citra 1 : ', citra2.shape)

fig, axes = plt.subplots(1, 2, figsize=(10, 10)) #membuat subplot dengan ukuran 1x2 dan size 10x10
ax = axes.ravel()  #Meratakan array dari objek subplot

ax[0].imshow(citra1, cmap='gray') #Memunculkan citra pertama
ax[0].set_title("Citra 1") #memberi judul
ax[1].imshow(citra2, cmap='gray') #Memunculkan citra kedua
ax[1].set_title("Citra 2") #memberi judul

#Menyiapkan variable output
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

# Melakukan proses Filter Median Pada Citra Input 1
for baris in range(0, m1-1): #untuk setiap baris dalam rentang 0 hingga m2-1 pada citra2
    for kolom in range(0, n2-1): #untuk setiap kolom dalam rentang 0 hingga n2-1 pada citra2
        a1 = baris  # variabel a1 menjadi nilai baris
        b1 = kolom  # variabel b1 menjadi nilai kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1], \
              copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1], \
              copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]] # Mendapatkan nilai piksel di sekitar piksel (a1, b1) dalam citra2

        # Urutkan
        for i in range(1, 8): #untuk i dalam rentang 1 hingga 7
            for j in range(i, 9): #untuk j dalam rentang i hingga 8
                if dataA[i] > dataA[j]:  # Jika nilai dataA[i] lebih besar dari dataA[j]
                    tmpA = dataA[i]  # Tukar nilai dataA[i] dengan dataA[j]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output1[a1, b1] = dataA[5]  # Mengisi nilai piksel (a1, b1) pada output2 dengan nilai median dari dataA
        
# Melakukan proses Filter Median Pada Citra Input 2 
for baris in range(0, m2-1):  #untuk setiap baris dalam rentang 0 hingga m2-1 pada citra2
    for kolom in range(0, n2-1):  #untuk setiap kolom dalam rentang 0 hingga n2-1 pada citra2
        a1 = baris  #variabel a1 menjadi nilai baris
        b1 = kolom  #variabel a1 menjadi nilai kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1], \
              copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1], \
              copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]] 
        #Mendapatkan nilai piksel di sekitar piksel (a1, b1) dalam citra2

             # Urutkan
        for i in range(1, 8): #untuk i dalam rentang 1 hingga 7
            for j in range(i, 9): #untuk j dalam rentang i hingga 8
                if dataA[i] > dataA[j]:  # Jika nilai dataA[i] lebih besar dari dataA[j]
                    tmpA = dataA[i]  # Tukar nilai dataA[i] dengan dataA[j]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output2[a1, b1] = dataA[5]  # Mengisi nilai piksel (a1, b1) pada output2 dengan nilai median dari dataA
        
#Plot Citra Input dan Output Hasil dari Filter Rerata
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