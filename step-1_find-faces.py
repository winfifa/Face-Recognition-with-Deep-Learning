# -*- coding: utf-8 -*-
import dlib
from skimage import io
for index in range(1,4):
	path = "./pictures/"
	file_name = "facePicture"
	file_name += `index`
	file_name += ".jpg"
	file_picture = path + file_name
	face_detector = dlib.get_frontal_face_detector()
	win = dlib.image_window()
	image = io.imread(file_picture)
	detected_faces = face_detector(image, 1)
	win.set_image(image)

	for i, face_rect in enumerate(detected_faces):
		win.add_overlay(face_rect)
			            
	dlib.hit_enter_to_continue()
