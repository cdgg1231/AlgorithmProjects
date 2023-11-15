import cv2

video=cv2.VideoCapture(0) #default =0, external =1

fource= cv2.VideoWriter_fourcc(*'XVID')

output = cv2.VideoWriter('output.avi',fource, 30.0, (640,480))


while True:
    ret,frame=video.read() #will detect if cam is stable 
    output.write(frame)
    cv2.imshow("Camera",frame)
    k=cv2.waitKey(1) # k= keyboard:  O to manually close, 1= waiting from "q" key aka quit
    if k==ord('q'): #The ord() function returns the number representing the unicode code of a specified character
        break
video.release()
output.release()
cv2.destroyAllWindows
    