import cv2
img = cv2.imread("Lenna_(test_image).png")
print("image shape",img.shape)

cv2.imshow("Lenna", img)
imgResized = cv2.resize(img, (800,800))

#yeniden boyutlandırma
print("resized image shape",imgResized.shape)
cv2.imshow("Lenna_new_size", imgResized)

#kırpma
imgCropped = img[:200,:300]
cv2.imshow("Lenna_cropped", imgCropped)