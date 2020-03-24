import cv2
import numpy as np
import sys
import os

def compare(image, reference):
    '''
    :param image:
    :param reference:
    :return: Boolean for whether the webcam image is a match with the reference image.
    '''


def login():
    '''
    Logs into Windows
    :return:
    '''

def takeReferenceImage(webcam):
    '''
    :param webcam: VideoCapture object for the webcam
    :return: Reference image
    '''
    ret, image = webcam.read()
    image = cv2.flip(image, 1)
    cv2.imwrite('D:\Projects\smile\img\\ref.jpg', image)
    webcam.release()
    return image

def main():
    # initializes webcam
    webcam = cv2.VideoCapture(0)

    reference = takeReferenceImage(webcam)

    print(reference.shape)

    # while True:
    #     ret, image = webcam.read()
    #
    #     if not ret:
    #         print("Webcam failed.")
    #         sys.exit(0)
    #
    #     if compare(image, reference):
    #         # closes webcam
    #         webcam.release()
    #         login()
    #
    #     cv2.imshow("capture", image)
    #     cv2.waitKey(0)

    #webcam.release()


if __name__ == '__main__':
    main()
