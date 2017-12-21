#To access pi cam
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

#For QR scan
import zbar
from PIL import Image
import cv2

# allow the camera to warmup
time.sleep(0.1)


def main():

    # Begin capturing video.
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    while True:
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
		for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	    	# grab the raw NumPy array representing the image, then initialize the timestamp
	    	# and occupied/unoccupied text
	    	image = frame.array

		    # show the frame
		    cv2.imshow("Frame", image)
		    key = cv2.waitKey(1) & 0xFF

		    # clear the stream in preparation for the next frame
		    rawCapture.truncate(0)

        # Converts image to grayscale.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        image2 = Image.fromarray(gray)
        width, height = image.size
        zbar_image = zbar.Image(width, height, 'Y800', image2.tobytes())

        # Scans the zbar image.
        scanner = zbar.ImageScanner()
        scanner.scan(zbar_image2)

        # Prints data from image.
        for decoded in zbar_image:
            print(decoded.data)


if __name__ == "__main__":
    main()