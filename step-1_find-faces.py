# -*- coding: utf-8 -*-
import os, os.path
#如果没有安装dlib，按下列步骤安装
#yum install boost-devel 
#yum install make
#pip install cmake
#pip install dlib 
import dlib
from skimage import io

DIR = "./pictures/"
for name in os.listdir(DIR):
	if os.path.isfile(os.path.join(DIR, name)):
		face_detector = dlib.get_frontal_face_detector()
		win = dlib.image_window()
		image = io.imread(os.path.join(DIR, name))
		detected_faces = face_detector(image, 1)
		win.set_image(image)

		for i, face_rect in enumerate(detected_faces):
			win.add_overlay(face_rect)
					        
		dlib.hit_enter_to_continue()
