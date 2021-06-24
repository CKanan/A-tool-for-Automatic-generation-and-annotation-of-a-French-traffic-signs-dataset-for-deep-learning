from functions import *


parent_dir = create_dir('image',os.getcwd())

stop_sign = cv2.CascadeClassifier('stop.xml') 
# stop_id=1
stop_path=create_dir('stop_img',os.path.split(parent_dir)[1])
stop_count=1

cameraCapture = cv2.VideoCapture('france.mp4') 
cv2.namedWindow('Window')

success, frame = cameraCapture.read()


# while success and not clicked:
while success:
    
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    stop_found = stop_sign.detectMultiScale(img_gray)

    stop_count=img_properties(stop_found,frame,stop_count,stop_path)
    
    cv2.imshow('Window', frame)
    success, frame = cameraCapture.read()
    
    if cv2.waitKey(1) & 0Xff == ord('q'):
      break


cv2.destroyAllWindows()
cameraCapture.release()