# import cv2
# cam = cv2.VideoCapture(1)
# frame = cam.read()[1]
# cv2.imwrite(filename='img.jpeg', img=frame)
# cam.release()
import cv2

# Camera 0 is the integrated web cam on my netbook
camera_port = 0

# Number of frames to throw away while the camera adjusts to light levels


# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)


# Captures a single image from the camera and returns it in PIL format

# Take the actual image we want to keep
camera_capture = camera.read()[1]
file = "test_image.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, img=camera_capture)

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del (camera)