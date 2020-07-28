#First open the image
#Now convert the colouerd into grayscale by following method =B*0.2989+G*0.5870+R*0.1140
#repalce the average value in r,g,b in pixel the coloured image
from PIL import Image
import numpy as np
# opens the image
image=Image.open('flower.jpeg')
#converting the image into array
image_array=np.array(image)
#Now taking the average of each pixel in the image
for i in range(image.height):
    for j in range(image.width):
        average=(image_array[i][j][0]*0.2989+image_array[i][j][1]*0.5870+image_array[i][j][2]*0.1140)
        image_array[i][j][0]=average
        image_array[i][j][1]=average
        image_array[i][j][2]=average
new_img=Image.fromarray(image_array,'RGB')
new_img.show()                                          
