print(f'lesson11\n')

import cv2

image_path = '3xcats.jpg'

handle_cat_face = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)


cat_face_data = handle_cat_face.detectMultiScale(image)
# print(cat_face_data)

colors = [(0, 255, 255), (0, 255, 0), (0, 0, 255)]
i = 0
for (x, y, w, h) in cat_face_data:
    cv2.rectangle(image, (x, y), (x+w, y+h), colors[i], 3)
    i += 1

cv2.imshow('cat',image)
cv2.waitKey()
cv2.rec