import cv2 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) 

while 1: 

 ret, img = cap.read() 
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

 faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
 for (x,y,w,h) in faces: 
  
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
  roi_gray = gray[y:y+h, x:x+w] 
  roi_color = img[y:y+h, x:x+w] 

 # Display an image in a window 
 cv2.imshow('img',img) 

 # Wait for Esc key to stop 
 if cv2.waitKey(1) & 0xFF == ord('q'):
  break

# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 

