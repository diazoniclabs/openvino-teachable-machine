# image-classification-teachable-machine

Step 1: Go to Teachable Machine and train an image classification model
Step 2: Download the Keras model file (.h5 file type)
Step 3: Convert Keras model (.h5 file type) to Tensorflow model (.pb Graph file type) using h5 to pb model converter notebook ( Use Google Colab )
Step 4: Use tf-cv file for running model on Opencv DNN library
(Optional) Step 5: Convert the (.pb) model into (.xml) and (.bin) file using model optimizer

pip install openvino-dev
!mo --input_model /content/frozen_models/final_model.pb --input_shape "[1,224,224,3]" --data_type=FP16

Inspired by : # https://github.com/opencv/opencv/issues/16582
