# import cv2 as cv
from deepface import DeepFace
import cv2

#==============================================
#Capturing image using openCV
#==============================================

cap = cv2.VideoCapture(0)
cap.set(3, 640) #width = 640
cap.set(4, 480) #height = 480

if cap.isOpened():
   _,frame = cap.read()
   cap.release() #releasing camera immediately after capturing picture
   if _ and frame is not None:
        cv2.imwrite('image.jpg', frame)

#=======================================
# Extract faces from document

image2 = cv2.imread('./voterid.jpg')
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

image2 = cv2.imread('./f00.jpg')
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces1 = facesCascade.detectMultiScale(
    gray1,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30) 
)

face2 = faceCascade.detectMultiScale(
   gray2,
   scaleFactor=1.3,
   minNeighbors=3,
   minSize=(30, 30))

for (x, y, w, h) in faces1:
    cv2.rectangle(image1, (x,y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image1[y:y + h, x:x +w]
    cv2.imwrite('image.jpg', roi_color)
for (x, y, w, h) in face2:
    cv2.rectangle(image2, (x,y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image2[y:y + h, x:x + w]
    cv2.imwrite('image2.jpg', roi_color)


#=============================================
# Image comparision using Deep face

models = [
    "VGG-Face",
    "Facenet",
    "Facenet512"
    "OpenFace"
    "DeepFace"
    "DeepID"
    "ArcFace"
    "Dlib"
    "SFace"
]

#Face Verification
result = DeepFace.verify(img1_path = "image.jpg",
      img2_path = "image_2.jpg",
      model_name = models[0]
)

print("=======================================================")
if result['verified']:
    print("Facial Authentication Successfull")
else:
    print("Incorrect customer details. Please re-verify")

# print(result)





