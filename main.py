print(f'lesson11\n')

import cv2

image_path = '394064.jpeg'
image = cv2.imread(image_path)
cv2.imshow('cat',image)
cv2.waitKey()