import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img(source):
    img = cv2.imread(source).astype(np.float32) / 255
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display_img(frame,image):
    
    while True:
        
        cv2.imshow(frame,image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cv2.destroyAllWindows()   
        
img = load_img(source='sammy.jpg')
display_img('sammy',img)

noise_img = load_img(source='sammy_noise.jpg')
display_img('noise-sammy',noise_img)

median = cv2.medianBlur(noise_img,5)
display_img('median',median)