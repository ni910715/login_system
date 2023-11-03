import cv2
import os
import uuid

video=cv2.VideoCapture(2)

nameID=str(input("Enter Your Name: ")).lower()
# path='/home/ni/vgg16_keras/images/'+nameID
# path='/home/ni/vgg16_keras/images/valid/'+nameID
# path='/home/ni/vgg16_keras/images/train/'+nameID
path='/home/ni/vgg16_keras/'+nameID

isExist = os.path.exists(path)

if isExist:
	print("Name Already Taken")
	nameID=str(input("Enter Your Name Again: "))
else:
	os.makedirs(path)
count = 0
while True:
	ret,frame=video.read()
	frame = frame[120:120+224,200:200+224, :]
	# if cv2.waitKey(1) & 0XFF == ord('a'):
	if cv2.waitKey(1) & count < 500:
		# name=path+'/'+ str(count) + '.jpg'
		uid = uuid.uuid4()
		name=path+'/'+ str(uid) + '.jpg'
		# name='./images/'+nameID+'/'+ str(count) + '.jpg'
		print("Creating Images........." +name)
		cv2.imwrite(name, frame)
		count += 1
	cv2.imshow('Image Collection', frame)

	if cv2.waitKey(1) & 0XFF == ord('q'):
		break

video.release()
cv2.destroyAllWindows()