import cv2
import numpy as np


#resim olustur

image = np.zeros((512,512,3), np.uint8) #siyah bir resime karşılık geliyor.
print(image.shape)


cv2.imshow("Siyah", image)

# cizgi
# (resim, başlangıç noktasi, bitiş noktasi,renk,  kalınlık)
cv2.line(image,(100,100), (100,300), (0,255,0), 3) # BGR((0,255,0)  Yeşil renk ortadaki (Blue, Green,Red)
cv2.imshow("Cizgi", image)

#dikdortgen
#resim, başlangıç, bitiş, renk

cv2.rectangle(image, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Dıkdortgen", image)

#cember
# resim, merkez, yarıçapı, renk
cv2.circle(image, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Cember", image)


#metin
# resim, baslangic noktasi, font,kalınlıgı, renk

cv2.putText(image, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255))
cv2.imshow("Metin", image)