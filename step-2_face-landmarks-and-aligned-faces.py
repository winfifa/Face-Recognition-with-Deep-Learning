# -*- coding: utf-8 -*-
import os, os.path
#如果没有安装dlib，按下列步骤安装
#yum install boost-devel 
#yum install make
#pip install cmake
#pip install dlib 
import dlib
#如果没有安装cv2，按下列步骤安装
#pip install opencv-python
import cv2
#如果没有安装openface,按下列步骤安装
#git clone https://github.com/cmusatyalab/openface.git
#cd openface
#pip install -r requirements.txt
#sudo python setup.py install
import openface
from skimage import io

predictor_model = "shape_predictor_68_face_landmarks.dat"
DIR = "./pictures/"

for name in os.listdir(DIR):
	if os.path.isfile(os.path.join(DIR, name)):
		face_detector = dlib.get_frontal_face_detector()
		face_pose_predictor = dlib.shape_predictor(predictor_model)
		face_aligner = openface.AlignDlib(predictor_model)

		image = cv2.imread(os.path.join(DIR, name))
		detected_faces = face_detector(image, 1)

		for i, face_rect in enumerate(detected_faces):
			pose_landmarks = face_pose_predictor(image, face_rect)
			alignedFace = face_aligner.align(534, image, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
			cv2.imwrite(os.path.join(DIR, "aligned_face_{}.jpg".format(i)), alignedFace)

			alignedPicture = io.imread(os.path.join(DIR, "aligned_face_{}.jpg".format(i)))
			#下面的代码只是为了加载纠正过的图片并把原来的标识打在图片上方便看区别，可以注释掉		
			win = dlib.image_window()
			win.set_image(alignedPicture)
			win.add_overlay(face_rect)
			win.add_overlay(pose_landmarks)	        
			dlib.hit_enter_to_continue()
