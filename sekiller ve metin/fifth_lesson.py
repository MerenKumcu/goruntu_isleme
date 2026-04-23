import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img2 = np.zeros((512,512,3),np.uint8)
cv2.imshow("deneme", img)

#çizgi çekmek
cv2.line(img, (0,0), (512,512), (255,0,0),3)
#cv2.line(resim,(başlagıç noktası),(bitiş noktası),(renk),kalınlık)
cv2.imshow("renkli_deneme", img)

cv2.line(img2, (512,0), (0,512), (255,0,0),3)
cv2.imshow("renkli_deneme_2", img2)

#dikdörtgen çizmek
#cv2.rectangle(resim,başlangıç, bitiş, renk, cv2.FILLED(doldurmak istersek))
cv2.rectangle(img, (15,15),(400,400), (0,255,0))
cv2.imshow("dikdortgen_deneme", img)

cv2.rectangle(img2, (15,15),(400,400), (0,255,0),cv2.FILLED)
cv2.imshow("dikdortgen_deneme2", img2)

#çember
cv2.circle(img, (270,270), 30, (0,0,255))
cv2.imshow("cember_deneme", img)
#daire
cv2.circle(img2, (270,270), 30, (0,0,255),cv2.FILLED)
cv2.imshow("daire_deneme", img2)

#yazı
cv2.putText(img, "deneme", (300,300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("yazi_deneme", img)