import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
import numpy as np #mengimport library numpy untuk array dan matriks
import cv2 #library untuk operasi dalam citra
from skimage import data    #Mengimport submodul data dari skimage untuk mengakses dataset citra
from skimage.io import imread    #Mengimport fungsi imread dari submodul io skimage untuk membaca citra
from skimage.color import rgb2gray #Mengimpor fungsi rgb2gray dari modul skimage.color untuk mengubah citra menjadi citra grayscale

citra1 = cv2.imread("mobil.jpeg", cv2.IMREAD_GRAYSCALE) #membuka gambar1 dengan opencv dalam pembacaan grayscale
citra2 = cv2.imread("boneka2.jpeg", cv2.IMREAD_GRAYSCALE) #membuka gambar2 dengan opencv dalam pembacaan grayscale

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
copyCitra1 = citra1.copy() #membuat copy dan menjadi citra1 kedalam plot-plot dalam hasil output
copyCitra2 = citra2.copy() #membuat copy dan menjadi citra2 kedalam plot-plot dalam hasil output

#Mendapatkan dimensi citra1 hasil copy
m1, n1 = copyCitra1.shape #m1 untuk baris dan ni untuk jumlah kolom
output1 = np.empty([m1, n1]) #Membuat array kosong dengan ukuran m1 x n1 dan menyimpannya ke dalam variabel output1
#Mendapatkan dimensi citra2 hasil copy
m2, n2 = copyCitra2.shape #m1 untuk baris dan ni untuk jumlah kolom
output2 = np.empty([m2, n2]) #Membuat array kosong dengan ukuran m1 x n1 dan menyimpannya ke dalam variabel output2

# Mencetak dimensi copy citra 1 dan output citra 1
print('Shape copy citra 1:', copyCitra1.shape)
print('Shape output citra 1:', output1.shape) #menampilkan dimensi output citra 1
print('m1:', m1) #mencetak nilai baris
print('n1:', n1) #mencetak nilai kolom
print()

# Mencetak dimensi copy citra 1 dan output citra 2
print('Shape copy citra 2:', copyCitra2.shape)
print('Shape output citra 2:', output2.shape) #menampilkan dimensi output citra 1
print('m2:', m2) #mencetak nilai baris
print('n2:', n2) #mencetak nilai kolom
print()

# Melakukan proses Filter Median Pada Citra Input 1
for baris in range(0, m1 - 1):  #untuk setiap baris dalam rentang 0 hingga m2-1 pada citra2
    for kolom in range(0, n1 - 1): #untuk setiap kolom dalam rentang 0 hingga n2-1 pada citra2

        a1 = baris #variabel a1 menjadi nilai baris
        b1 = kolom #variabel b1 menjadi nilai kolom

        arr = np.array([copyCitra1[a1 - 1, b1 - 1], copyCitra1[a1 - 1, b1], copyCitra1[a1, b1 + 1], \
                        copyCitra1[a1, b1 - 1], copyCitra1[a1, b1 + 1], copyCitra1[a1 + 1, b1 - 1], \
                        copyCitra1[a1 + 1, b1], copyCitra1[a1 + 1, b1 + 1]])    # Membuat array yang berisi nilai piksel tetangga

        minPiksel = np.amin(arr)    # Menentukan nilai piksel minimum
        maksPiksel = np.amax(arr)    # Menentukan nilai piksel maksimum

        if copyCitra1[baris, kolom] < minPiksel:    # Jika piksel saat ini kurang dari nilai piksel minimum
            output1[baris, kolom] = minPiksel    # Set nilai output citra 1 sebagai nilai piksel minimum
        else:
            if copyCitra1[baris, kolom] > maksPiksel:    # Jika nilai piksel saat ini lebih dari nilai piksel maksimum
                output1[baris, kolom] = maksPiksel    # Set nilai output citra 1 sebagai nilai piksel maksimum
            else:
                output1[baris, kolom] = copyCitra1[baris, kolom]    # Set nilai output citra 1 sebagai nilai piksel saat ini

for baris1 in range(0, m2 - 1): #untuk setiap baris dalam rentang 0 hingga m2-1 pada citra2
    for kolom1 in range(0, n2 - 1): #untuk setiap kolom dalam rentang 0 hingga n2-1 pada citra2

        a1 = baris1 #variabel a1 menjadi nilai baris
        b1 = kolom1 #variabel b1 menjadi nilai kolom

        arr = np.array([copyCitra2[a1 - 1, b1 - 1], copyCitra2[a1 - 1, b1], copyCitra2[a1, b1 + 1], \
                        copyCitra2[a1, b1 - 1], copyCitra2[a1, b1 + 1], copyCitra2[a1 + 1, b1 - 1], \
                        copyCitra2[a1 + 1, b1], copyCitra2[a1 + 1, b1 + 1]]) #Membentuk array dengan nilai piksel di sekitar piksel saat ini

        minPiksel = np.amin(arr) # Mendapatkan nilai piksel minimum 
        maksPiksel = np.amax(arr) # Mendapatkan nilai piksel maksimum dari array

        if copyCitra2[baris1, kolom1] < minPiksel: #Jika piksel saat ini kurang dari nilai piksel minimum
            output2[baris1, kolom1] = minPiksel    #Set nilai output citra 2 sebagai nilai piksel minimum
        else:
            if copyCitra2[baris1, kolom1] > maksPiksel:    #Jika nilai piksel saat ini lebih dari nilai piksel maksimum
                output2[baris1, kolom1] = maksPiksel    #Set nilai output citra 2 sebagai nilai piksel maksimum
            else:
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]    # Set nilai output citra 2 sebagai nilai piksel saat ini
                
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