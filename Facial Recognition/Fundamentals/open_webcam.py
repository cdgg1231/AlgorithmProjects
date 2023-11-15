import cv2

video=cv2.VideoCapture(0) #default =0, external =1



print(video.get(cv2.CAP_PROP_FRAME_WIDTH)) # get = gives back frame dimension
print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

video.set(3,1000) # Make frame width bigger 
video.set(4,500)  # height


while True:
    ret,frame=video.read() #will detect if cam is stable 
    cv2.imshow("Camera",frame)
    k=cv2.waitKey(1) # k= keyboard:  O to manually close, 1= waiting from "q" key aka quit
    if k==ord('q'): #The ord() function returns the number representing the unicode code of a specified character
        break
video.release()
cv2.destroyAllWindows
    