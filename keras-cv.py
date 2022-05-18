from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

label = ['Ameer','Phone']

import cv2
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):
	ret, frame = vid.read()
	cv2.imwrite('x.jpg',frame)
	size = (224, 224)
	image = Image.open('x.jpg')
	image = ImageOps.fit(image, size, Image.ANTIALIAS)
	image_array = np.asarray(image)
	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
	data[0] = normalized_image_array
	#data[0] = frame
	prediction = model.predict(data)
	op = np.argmax(prediction[0])
	op = label[op]
	p = np.max(prediction[0])*100
	p = np.round(p,2)
	#print(p)
	cv2.putText(frame,f'{op}-{p}%',(30,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

