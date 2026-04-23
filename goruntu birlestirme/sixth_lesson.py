import cv2
import numpy as np
img = cv2.imread("Lenna.png")
cv2.imshow("first", img)

hor = np.hstack((img,img))
cv2.imshow("second", hor)

ver = np.vstack((img,img))
cv2.imshow("third", ver)
