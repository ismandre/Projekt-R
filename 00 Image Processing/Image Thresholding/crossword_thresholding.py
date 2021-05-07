import cv2
import matplotlib.pyplot as plt

img = cv2.imread('crossword.jpg',0)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 540,720)

cv2.namedWindow('binary',cv2.WINDOW_NORMAL)
cv2.resizeWindow('binary', 540,720)

cv2.namedWindow('adaptive',cv2.WINDOW_NORMAL)
cv2.resizeWindow('adaptive', 540,720)

cv2.namedWindow('blended',cv2.WINDOW_NORMAL)
cv2.resizeWindow('blended', 540,720)

ret,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)

blended = cv2.addWeighted(src1=th1,alpha=0.6,src2=th2,beta=0.4,gamma=0)

while True:
    
    cv2.imshow('blended',blended)
    cv2.imshow('adaptive',th2)
    cv2.imshow('binary',th1)
    cv2.imshow('image',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()
