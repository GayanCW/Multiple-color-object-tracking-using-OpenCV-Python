import cv2
import numpy as np

# capturing video through webcam
cap = cv2.VideoCapture(0)
# area
a = 3000

while (1):
    _, img = cap.read()

    # converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # defining the Range of yellow color
    yellow_lower = np.array([11, 83, 225], np.uint8)
    yellow_upper = np.array([123, 109, 255], np.uint8)

    # defining the Range of Green color
    green_lower = np.array([42, 32, 95], np.uint8)
    green_upper = np.array([76, 93, 176], np.uint8)

    # definig the range of red color
    red_lower = np.array([0, 91, 172], np.uint8)
    red_upper = np.array([5, 149, 227], np.uint8)

    # defining the Range of Orange color
    orange_lower = np.array([7, 0, 195], np.uint8)
    orange_upper = np.array([11, 255, 255], np.uint8)

    # defining the Range of blue color
    blue_lower = np.array([79, 142, 97], np.uint8)
    blue_upper = np.array([255, 255, 255], np.uint8)

    # defining the Range of purple color
    purple_lower = np.array([109, 67, 114], np.uint8)
    purple_upper = np.array([255, 107, 255], np.uint8)

    # finding the range of colors in the image
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green = cv2.inRange(hsv, green_lower, green_upper)
    red = cv2.inRange(hsv, red_lower, red_upper)
    orange = cv2.inRange(hsv, orange_lower, orange_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    purple = cv2.inRange(hsv, purple_lower, purple_upper)

    # Morphological transformation, Dilation
    kernal = np.ones((5, 5), "uint8")

    yellow = cv2.dilate(yellow, kernal)
    green = cv2.dilate(green, kernal)
    red = cv2.dilate(red, kernal)
    orange = cv2.dilate(orange, kernal)
    blue = cv2.dilate(blue, kernal)
    purple = cv2.dilate(purple, kernal)

    ###############################################################

    # Tracking the Blue Color
    contours, hierarchy = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > a):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # Tracking the yellow Color
    contours, hierarchy = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > a):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # Tracking the Green Color
    contours, hierarchy = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > a):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Green", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # Tracking the Red Color
    contours, hierarchy = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > a):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # Tracking the Orange Color
    contours, hierarchy = cv2.findContours(orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > a):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Orange", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # Tracking the Purple Color
    contours, hierarchy = cv2.findContours(purple, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > a):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Purple", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
