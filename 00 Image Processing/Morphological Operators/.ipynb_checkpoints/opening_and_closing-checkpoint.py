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

# BACK GROUND NOISE EROSION

white_noise = np.random.randint(low=0,high=2,size=(600,600))
white_noise = white_noise * 255

noise_img = white_noise + img
display_img('noised',noise_img)

# OPENING
kernel = np.ones((5,5),dtype=np.uint8)
opening = cv2.morphologyEx(noise_img,cv2.MORPH_OPEN,kernel)
display_img('opening',opening)

# FORE GROUND NOISE EROSION

img = load_img()
black_noise = np.random.randint(low=0,high=2,size=(600,600))
black_noise = black_noise * -255

black_noise_img = img + black_noise
black_noise_img[black_noise_img == -255] = 0
display_img('b_noised',black_noise_img)

# CLOSING

closing = cv2.morphologyEx(black_noise_img,cv2.MORPH_CLOSE, kernel)
display_img('closed',closing)