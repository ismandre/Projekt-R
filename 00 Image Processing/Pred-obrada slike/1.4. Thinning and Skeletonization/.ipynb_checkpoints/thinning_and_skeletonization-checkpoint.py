import cv2
import numpy as np

img = cv2.imread('b.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 5)

while True:
    
    cv2.imshow('frame1',erosion)
    cv2.imshow('frame2',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()