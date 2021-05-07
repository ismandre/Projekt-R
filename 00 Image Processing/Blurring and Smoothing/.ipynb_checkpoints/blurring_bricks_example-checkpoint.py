import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img(source):
    img = cv2.imread('bricks.jpg').astype(np.float32) / 255
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display_img(frame,image):
    
    while True:
        
        cv2.imshow(frame,image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cv2.destroyAllWindows()   
        
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(0,0,255),thickness=4)

display_img('with_text',img)

# CUSTOM BLUR

kernel = np.ones(shape=(5,5),dtype=np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
display_img('blurred1',dst)

# BUILT-IN OPENCV BLUR

img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(0,0,255),thickness=4)

blurred = cv2.blur(img,ksize=(10,10))
display_img('built-in-blur',blurred)

# GAUSSIAN AND MEDIAN BLURRING

img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(0,0,255),thickness=4)

blurred_g = cv2.GaussianBlur(img,(5,5),10)
display_img('blurred-gaussian',blurred_g)

blurred_m = cv2.medianBlur(img,5)
display_img('blurred-median',blurred_m)