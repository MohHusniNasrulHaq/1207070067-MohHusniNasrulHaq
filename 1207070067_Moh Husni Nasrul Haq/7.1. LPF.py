import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
import numpy as np #mengimport library numpy untuk array dan matriks
import cv2 #library untuk operasi dalam citra

img = cv2.imread('prabowo.jpeg') #membuka gambar dengan opencv

prabowo = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # mengubah format gambar dari BGR menjadi RGB

plt.imshow(img) #menampilkan gambar asli tanpa filter
# Membuat filter: matriks berukuran 5 x 5 dengan nilai semua elemen 1/25
kernel = np.ones((5,5), np.float32) / 25
print(kernel) #menampilkan hasil operasi kernel


prabowo_filter = cv2.filter2D(img, -1, kernel) #melakukan proses filtering dengan filter awal


plt.rcParams["figure.figsize"] = (15,15) #memperbesar ukuran hasil plotting jika diperlukan

# Plot pertama, gambar asli
plt.subplot(121) #ngesubplot dengan matriks 1x2 dan tampil di citra grafik1
plt.imshow(prabowo) #menampilkan citra
plt.title('Original') #memberi judul
plt.xticks([]), plt.yticks([])

# Plot kedua, hasil filter dengan kernel awal
plt.subplot(122) #ngesubplot dengan matriks 1x2 dan tampil di citra grafik2
plt.imshow(prabowo_filter) #menampilkan citra
plt.title('Averaging') #memberi judul
plt.xticks([]), plt.yticks([])

# Tampilkan plot
plt.show() #menampilkan seluruh citra

# Blur menggunakan fungsi cv2.blur pada gambar asli
prabowo_blur = cv2.blur(prabowo, (5, 5))

# Membuat kernel dengan np.matrix
kernel_new = np.matrix([[1, 1, 1],
                    [1, 2, 1],
                    [1, 1, 1]]) / 25

# Lakukan proses filtering dengan kernel baru pada gambar asli
prabowo_filter_new = cv2.filter2D(prabowo, -1, kernel_new)

# Tampilkan gambar awal, hasil filter, hasil blur, dan hasil filter baru secara bersamaan
plt.figure(figsize=(15, 10))

# Gambar awal
plt.subplot(221)  #ngesubplot dengan matriks 2x2 dan tampil di citra grafik1
plt.imshow(prabowo) #menampilkan citra
plt.title("Original")  #memberi judul

# Hasil filter
plt.subplot(222)  #ngesubplot dengan matriks 2x2 dan tampil di citra grafik2
plt.imshow(prabowo_filter)  #menampilkan citra
plt.title("Averaging")  #memberi judul

# Hasil blur
plt.subplot(223)  #ngesubplot dengan matriks 2x2 dan tampil di citra grafik3
plt.imshow(prabowo_blur) #menampilkan citra
plt.title("Gambar Blur") #memberi judul

# Hasil filter baru
plt.subplot(224) #ngesubplot dengan matriks 2x2 dan tampil di citra grafik3
plt.imshow(prabowo_filter_new) #menampilkan citra
plt.title("Gambar Filtering Kernel Baru") #memberi judul

plt.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show() #memunculkan seluruh operasi citra 