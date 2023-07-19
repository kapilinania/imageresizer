import cv2
source_Data = '1.jpg'
dest_Data = 'newimage.png'
# we can convert images source png jpg jpeg any kind of images we can do that
scale_percent = 50

imageData = cv2.imread(source_Data, cv2.IMREAD_UNCHANGED)

# help of user can easily show images
# cv2.imshow("title", imageData)

width = int(imageData.shape[1] * scale_percent / 100)
height = int(imageData.shape[0] * scale_percent / 100)

# resize
image_resize = (width, height)

# resize images
final_output = cv2.resize(imageData, image_resize)
cv2.imwrite(dest_Data, final_output)
cv2.waitKey(0)