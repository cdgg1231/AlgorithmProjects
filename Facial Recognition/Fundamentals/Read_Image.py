import cv2

img= cv2.imread("spiderman1.jpg", flags = 1)  # need to add a flag and give it a name holder "img" so you can call it

print(img)

cv2.imshow("Image",img)

cv2.waitKey(7000)
cv2.destroyAllWindows()

cv2.imwrite("gray_spriderman1.png", img)