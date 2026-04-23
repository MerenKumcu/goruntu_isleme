import cv2
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#blurring
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("origin")
plt.show()

#average blur

dst2 = cv2.blur(img, ksize=(3,3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("average blur")
plt.show()

#gaussian blur

gb = cv2.GaussianBlur(img, ksize = (3,3),  sigmaX= 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("gaussian blur")
plt.show()

#median blur
mb = cv2.medianBlur(img, ksize= 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("median blur")
plt.show()