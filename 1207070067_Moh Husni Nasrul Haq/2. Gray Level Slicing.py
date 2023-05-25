import cv2 #library untuk operasi dalam citra
import numpy as np #mengimport library numpy untuk array dan matriks
import matplotlib.pyplot as plt #mengimport library untuk menghasilkan grafik
#matplotlib inline

img = cv2.imread ('prabowo.jpeg', cv2.IMREAD_GRAYSCALE) #membuka gambar dengan opencv dalam pembacaan grayscale

row, column = img.shape #dimensi cita yang diinputkan

img1 = np.zeros((row,column),dtype = 'uint8')
 
# menerapkan Min-Max nilai kontras citra grayscale
min_range = 10
max_range = 60
 
#operasi untuk setting jika rangenya sama dengan 255 maka putih dan jika 0 maka hitam
for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 255
        else:
            img1[i,j] = 0
            
#Plot Image
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) #membuat subplot dengan ukuran 2x2 dan size 12x12
ax = axes.ravel() # Meratakan array dari objek subplot

ax[0].imshow(img, cmap=plt.cm.gray) #memunculkan hasil citra di subplot 1
ax[0].set_title("Citra Input") #memberi judul
ax[1].hist(img.ravel(), bins=256) #memunculkan operasi citra hasil grafik histogram dalam subplot 2
ax[1].set_title('Histogram Input') #memberi judul

ax[2].imshow(img1, cmap=plt.cm.gray) #memunculkan hasil citra di subplot 3
ax[2].set_title("Citra Output") #memberi judul
ax[3].hist(img1.ravel(), bins=256) #memunculkan operasi citra hasil grafik histogram dalam subplot 4 
ax[3].set_title('Histogram Output')#memberi judul

fig.tight_layout() #menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show() #memunculkan seluruh operasi citra 