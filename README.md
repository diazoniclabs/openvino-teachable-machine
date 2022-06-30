# Model Deployment of Binary Image Classification on Edge

![image](https://user-images.githubusercontent.com/61781809/176463362-a20fc6c0-5edc-4e16-b9b0-03e7efb49901.png)

**Step 1**: Go to Teachable Machine and train an image classification model
Link : [Teachable Machine](https://teachablemachine.withgoogle.com/)

**Step 2**: Download the Keras model file (.h5 file type) from Teachable Machine
![image](https://user-images.githubusercontent.com/61781809/176611918-e9c03c99-50ed-4932-892f-0857199a26b0.png)

**Step 3**: Convert Keras model (.h5 file type) to Tensorflow model (.pb Graph file type) using h5 to pb model converter notebook ( Use Google Colab )

**Step 4**: Use tf-cv file for running model on Opencv DNN library

**(Optional) Step 5**: Convert the (.pb) model into (.xml) and (.bin) file using model optimizer

```
pip install openvino-dev[tensorflow2]==2021.4.2

!mo --input_model /content/frozen_models/final_model.pb --input_shape "[1,224,224,3]" --data_type=FP16 --output_dir /content
```

# How to run the python file?
```
python tf-cv-new.py --input_xml tf_final.xml --input_bin tf_final.bin
```

Inspired by : 

[Click here](https://github.com/opencv/opencv/issues/16582)


# Software Used : 
1. OpenVino Toolkit : 2021.4.2 Version 
