import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

img = plt.imread("a.jpg")

width = img.shape[0]
height = img.shape[1]

print(img.shape)
img = img.reshape(width * height, 3)

kmeans = KMeans(n_clusters=3).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

print(labels)
print(clusters)

img2 = numpy.zeros((width, height, 3), dtype=numpy.uint8)

index = 0
for i in range(width):
    for j in range(height):
        label_of_pixel = labels[index]
        img2[i][j] = clusters[label_of_pixel]
        index += 1
# cach 2
img3 = numpy.zeros_like(img)

for i in range(len(img3)):
	img3[i] = clusters[labels[i]]

img3 = img3.reshape(width,height,3)

plt.imshow(img3)
plt.show()
