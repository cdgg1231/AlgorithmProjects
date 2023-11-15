import cv2
import numpy as np

img= np.zeros((512,512,3), np.uint8) # mumpy creates an array of matrices, zero is all black
              # 3 is the channel 
#cv2.line(img,(0,20),(200,20),(0,255,0),2)
cv2.line(img,(0,40),(200,40),(0,255,0),2)
cv2.line(img,(0,60),(200,60),(0,255,0),2)
# (0,0) is the starting point, (120,120) is the ending point
#(x,y)
#BGR = BLUE, GREEN, RED (0,255,0), THICKESS

cv2.arrowedLine(img,(0,20),(200,20),(0,255,0),2)
cv2.circle(img,(155,155), 90, (255,0,0),-5) # to fill any shape dd a negative 
cv2.rectangle(img,(20,20), (500,100), (0,0,255), 4)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2= np.zeros((600,1000,3), np.uint8) 

cv2.rectangle(img2, (0,0), (1000,600), (255,255,255), -4)
cv2.circle(img2,(500,300),120, (0,0,255),-5) 
cv2.putText(img2, "Japan", (10,500), cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),3)


cv2.imshow("Japan", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()