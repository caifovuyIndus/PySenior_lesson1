print(f'lesson11\n')

import cv2

image_path = '394064.jpeg'

handle_cat_face = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)


cat_face_data = handle_cat_face.detectMultiScale(image)
print(cat_face_data)



cv2.imshow('cat',image)
cv2.waitKey()