import cv2
img = cv2.imread("ricardo.webp",0)

cv2.imshow("first picture", img)

k = cv2.waitKey(0) &0xFF

if k== 27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite("ricardo_gray.png", img)
    cv2.destroyAllWindows()