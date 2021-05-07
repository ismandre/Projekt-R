import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    blank_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=24)
    return blank_img

def display_img(frame,image):
    
    while True:
        
        cv2.imshow(frame,image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cv2.destroyAllWindows()   
        
img = load_img()
display_img('image',img)

# EROSION

kernel = np.ones((5,5),dtype=np.uint8)
result = cv2.erode(img,kernel,iterations=1)
display_img('eroded',result)

result4 = cv2.erode(img,kernel,iterations=4)
display_img('eroded4',result4)