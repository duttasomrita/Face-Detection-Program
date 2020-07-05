import cv2

#Create a CascadeClassifier Object:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Reading the image as it is:
img= cv2.imread("pp.jpg")

#Reading the image as GrayScale:
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search co-ordinates of the image:
faces=face_cascade.detectMultiScale(gray_img, 1.1, 4)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img= cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)


cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()