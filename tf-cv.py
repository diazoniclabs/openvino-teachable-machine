import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_xml', type=str, required=True)
parser.add_argument('--input_bin', type=str, required=True)

args = parser.parse_args()

#net = cv2.dnn.readNetFromTensorflow('final_model.pb')
net = cv2.dnn.readNet(args.input_xml,args.input_bin)

label = ['Category 1','Category 2']

net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) 

vid_cap = cv2.VideoCapture(0)
if not vid_cap.isOpened():
    raise IOError("Webcam cannot be opened!")

while True:
    # Capture frames
    ret, frame = vid_cap.read()
    inWidth = 224
    inHeight = 224
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0 / 255, size=(inWidth, inHeight),mean=(0, 0, 0))
    net.setInput(blob)
    out = net.forward()
    out = out.flatten()
    classId = np.argmax(out)
    confidence = np.round(out[classId]*100,2)
    op = f'{label[classId]} - {confidence}%'
    print(op)
    
    # For FPS and Inference Time
    cv2.putText(frame, op, (30,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
    t, _ = net.getPerfProfile()
    l = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
    cv2.putText(frame, l, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

# Release video capture object and close the window
vid_cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
