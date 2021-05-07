# fastNlMeansDenoisingColored
# Wait for result, takes time to respond
import cv2
from tkinter import filedialog
from tkinter import *

root = Tk()
# Do not show graphics window
# root.withdraw()

# Load the original color image
origColorImage = cv2.imread(filedialog.askopenfilename())

# Image must have 3 channels
print("Shape of image ", origColorImage.shape)

dest = cv2.fastNlMeansDenoisingColored(origColorImage,None,10,10,7,21)

while True: 
    cv2.imshow('Original image',origColorImage)
    cv2.imshow('fastNlMeansDenoisingColored',dest)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()