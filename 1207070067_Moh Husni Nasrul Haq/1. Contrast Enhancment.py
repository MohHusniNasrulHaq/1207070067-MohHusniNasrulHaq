import numpy as np #mengimport library numpy untuk array dan matriks
import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
#matplotlib inline
import matplotlib.image as mpimg
import cv2 #library untuk operasi dalam citra


img = cv2.imread ('dpr.jpeg', cv2.IMREAD_GRAYSCALE) #membuka gambar dengan opencv dalam pembacaan grayscale

image_equalized = cv2.equalizeHist(img) #memasukan histogram equalize kedalam citra yang tadi dibuka dalam grayscale

clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8)) #menerapkan kontras histogram equalization dalam citra yang digunakan dengan batasan matriks 8x8 
#Apply CLAHE to the original image
image_clahe = clahe.apply(img)


# menerapkan Min-Max nilai kontras citra grayscale
min_val = np.min(img)
max_val = np.max(img)
image_cs = 255 * (img - min_val) / (max_val - min_val) 

        
copyCamera = img.copy().astype(float) #membuat copy dan menjadi citra kedalam plot-plot dalam hasil output
output1 = copyCamera * 1.9 #membuat output yang dimana yaitu hasil operasi citra dikali dengan konstanta 1.9

        
fig, axes = plt.subplots(5, 2, figsize=(20, 20)) #membuat subplot dengan ukuran 5x2 dan size 20x20
ax = axes.ravel() # Meratakan array dari objek subplot

ax[0].imshow(img, cmap=plt.cm.gray) #memunculkan hasil citra di subplot 1
ax[0].set_title("Citra Input") #memberi judul
ax[1].hist(img.ravel(), bins=256) #memunculkan operasi citra hasil equalized dalam subplot 2
ax[1].set_title('Histogram Input') #memberi judul

ax[2].imshow(image_equalized, cmap=plt.cm.gray) #memunculkan hasil citra di subplot 3
ax[2].set_title("Citra Output HE") #memberi judul
ax[3].hist(image_equalized.ravel(), bins=256) #memunculkan operasi citra hasil equalized dalam subplot 4
ax[3].set_title('Histogram Output HE Method') #memberi judul

ax[4].imshow(image_cs, cmap=plt.cm.gray) #memunculkan hasil citra di subplot 5
ax[4].set_title("Citra Output CS")#memberi judul
ax[5].hist(image_cs.ravel(), bins=256)#memunculkan operasi citra hasil equalized dalam subplot 6
ax[5].set_title('Histogram Output CS Method')#memberi judul

ax[6].imshow(image_clahe, cmap=plt.cm.gray) #memunculkan hasil citra di subplot 7
ax[6].set_title("Citra Grayscale CLAHE")#memberi judul
ax[7].hist(image_clahe.ravel(), bins=256)#memunculkan operasi citra hasil equalized dalam subplot 8
ax[7].set_title('Histogram Output CLAHE Method')#memberi judul

ax[8].imshow(output1, cmap=plt.cm.gray) #memunculkan hasil citra di subplot 9
ax[8].set_title("Citra Grayscale Perkalian Konstanta")#memberi judul
ax[9].hist(output1.ravel(), bins=256)
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#memberi judul

fig.tight_layout() #menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show() #memunculkan seluruh operasi citra 