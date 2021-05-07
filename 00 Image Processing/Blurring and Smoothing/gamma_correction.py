import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    img = cv2.imread('bricks.jpg').astype(np.float32) / 255
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display_img(frame,image):
    
    while True:
        
        cv2.imshow(frame,image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cv2.destroyAllWindows()
    
def change_brightness(gamma,image):
    
    return np.power(image,gamma)
    
        
i = load_img()
display_img(frame='original',image=i)

brighter = change_brightness(1/4,i)
display_img(frame='bright',image=brighter)

darker = change_brightness(5,i)
display_img(frame='dark',image=darker)