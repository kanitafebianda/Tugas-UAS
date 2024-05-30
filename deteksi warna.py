import cv2
import numpy as np

def nothing(x):
    pass

#cv2.namedWindow("Tracking")

# Perulangan
while True:
    frame = cv2.imread('warna.png')
    if frame is None:
        print("Image not found.")
        break

    # Konversi warna BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Lower range warna kuning
    lower_range = np.array([20, 100, 100])

    # Upper range warna kuning
    upper_range = np.array([40, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Menampilkan gambar
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()