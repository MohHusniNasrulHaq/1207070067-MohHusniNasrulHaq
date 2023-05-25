import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
import numpy as np #mengimport library numpy untuk array dan matriks
import cv2 #library untuk operasi dalam citra

img = cv2.imread('prabowo.jpeg') #membuka gambar dengan opencv

# Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)  #Menggunakan operasi Laplace untuk high-pass filtering

# Sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=7) #Menggunakan opersi Sobel pada sumbu X 
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=7) #Menggunakan operasi Sobel pada sumbu Y 

# Perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (20, 20)

# Menampilkan citra asli
plt.subplot(2, 2, 1) #ngesubplot dengan matriks 2x2 dan tampil di citra grafik1
plt.imshow(img, cmap='gray') #memunculkan hasil citra grayscale
plt.title('Original') #memberi judul
plt.xticks([])  #Menghilangkan sumbu x
plt.yticks([])  #Menghilangkan sumbu y

# Menampilkan hasil Laplacian
plt.subplot(2, 2, 2) #ngesubplot dengan matriks 2x2 dan tampil di citra grafik2
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')  # Judul plot
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan hasil Sobel X
plt.subplot(2, 2, 3) #ngesubplot dengan matriks 2x2 dan tampil di citra grafik3
plt.imshow(sobelx, cmap='gray') #memunculkan hasil citra grayscale
plt.title('Sobel X') #memberi judul
plt.xticks([]) #Menghilangkan sumbu x
plt.yticks([]) #Menghilangkan sumbu y

# Menampilkan hasil Sobel Y
plt.subplot(2, 2, 4) #ngesubplot dengan matriks 2x2 dan tampil di citra grafik4
plt.imshow(sobely, cmap='gray') #memunculkan hasil citra grayscale
plt.title('Sobel Y') #memberi judul
plt.xticks([]) #Menghilangkan sumbu x
plt.yticks([]) #Menghilangkan sumbu y

plt.show()#Menampilkan plot


img = cv2.imread('minion.jpg',0) #Membaca citra sebagai grayscale

edges = cv2.Canny(img,100,200)#Memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)

# Menampilkan citra asli
plt.subplot(121)
plt.imshow(img,cmap = 'gray') #memunculkan hasil citra grayscale
plt.title('Original Image') #memberi judul
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

# Menampilkan citra hasil Canny Edges
plt.subplot(122)
plt.imshow(edges,cmap = 'gray') #memunculkan hasil citra grayscale
plt.title('Edge Image') #memberi judul
plt.xticks([])  # Menghilangkan sumbu x
plt.yticks([])  # Menghilangkan sumbu y

plt.show()#Menampilkan plot

# Image Thresholding