import cv2
img= cv2.imread("spiderman1.jpg", 1)

print(img.shape) # returns the dimension of image. 0= heigh, 1=width, 2= channel type(color BGR)
print(img.dtype) # possible color combos. starting with 0=black, 1=white
""" returns image d-type A UINT8 is an 8-bit unsigned integer 
from 0 to 255. As with all unsigned numbers, the values must 
be non-negative. Uint8's are mostly used in graphics (colors are always non-negative) """

print(type(img))


""" cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows() """