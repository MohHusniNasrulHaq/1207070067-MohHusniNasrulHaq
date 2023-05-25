import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
import numpy as np #mengimport library numpy untuk array dan matriks
import cv2 #library untuk operasi dalam citra

citra1 = cv2.imread("mobil.jpeg", cv2.IMREAD_GRAYSCALE) #membuka gambar1 dengan opencv dalam pembacaan grayscale
print(citra1.shape)  # Menampilkan dimensi citra1

plt.imshow(citra1, cmap='gray')  # Menampilkan citra1 dalam skala keabuan

kernel = np.array([[-1, 0, -1],  # Membuat kernel untuk filter sharpening
                   [0, 4, 0], 
                   [-1, 0, -1]])

citraOutput = cv2.filter2D(citra1, -1, kernel)  # Melakukan operasi filter sharpening pada citra1 dengan kernel yang telah dibuat

fig, axes = plt.subplots(1, 2, figsize=(12, 12))  # Membuat subplot dengan 1 baris dan 2 kolom untuk menampilkan citra input dan output
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 dalam skala keabuan pada sumbu x[0]
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap='gray')  # Menampilkan citraOutput dalam skala keabuan pada sumbu x[1]
ax[1].set_title("Citra Output")
plt.show()  # Menampilkan plot citra input dan output secara bersamaan