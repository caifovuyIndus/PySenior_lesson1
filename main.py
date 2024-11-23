print(f'lesson11\n')

import cv2
from PIL import Image

image_cat_path = '3xcats.jpg'
image_glasses_path = ''

handle_cat_face = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_cat_path)


cat_face_data = handle_cat_face.detectMultiScale(image)
print(cat_face_data)

cat = Image.open(image_cat_path).convert('RGB')
glasses = Image.open(image_glasses_path).convert('RGB')

colors = [(0, 255, 255), (0, 255, 0), (0, 0, 255)]
i = 0
for (x, y, w, h) in cat_face_data:
    glasses = glasses. resize(w, int(1/3))
    cat.paste(glasses, (x, int(y+h/4)))
    cat.cave('cat_with_glasses.jpg')
    # cv2.rectangle(image, (x, y), (x+w, y+h), colors[i], 3)
    # i += 1

# cv2.imshow('cat',image)
cat_with_glasses = cv2.imread('cat_with_glasses.jpg')
cv2.imshow('cat_with_glasses', cat_with_glasses)

cv2.waitKey()
cv2.rec