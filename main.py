import cv2
import face_recognition as fr
import numpy as np
import sys
from datetime import datetime
import os

REFERENCE_PATH = "D:\Projects\smile\images\\reference"


def compare(image, reference):
    """
    :param image: webcam image
    :param reference: reference image
    :return: Boolean for whether the webcam image is a match with the reference image.
    """

    # gets encoding for reference face
    reference_face_encoding = fr.face_encodings(reference)[0]
    # gets list of possible face encodings for unknown image
    image_face_encodings = fr.face_encodings(image)

    # draws rectangle around face
    # ref_face_location = fr.face_locations(reference)[0]
    # (top, right, bottom, left) = ref_face_location
    # # Draw a box around the face
    # cv2.rectangle(reference, (left, top), (right, bottom), (0, 0, 255), 2)
    # cv2.imshow('reference face', reference)

    # iterates through possible face encodings, and compares to reference.
    for face_encoding in image_face_encodings:
        matches = fr.compare_faces([reference_face_encoding], face_encoding)
        # if there is a face match, return True
        if True in matches:
            return True

    return False


def login():
    """
    Logs into Windows
    :return:
    """

    print('logged in!')
    return


def take_reference_image():
    """
    :return: Reference image
    """
    webcam = cv2.VideoCapture(0)
    ret, image = webcam.read()
    while not ret:
        ret, image = webcam.read()
    image = cv2.flip(image, 1)
    cv2.imwrite('D:\Projects\smile\images\\reference\{}.jpg'.format(datetime.now().strftime("%H%M%S")), image)
    webcam.release()
    return image


def main():
    reference = None

    # if nothing in reference images, then create a reference. else, grab reference from reference directory
    if len(os.listdir(REFERENCE_PATH)) == 0:
        reference = take_reference_image()
    else:
        for img in os.listdir(REFERENCE_PATH):
            print('{}\{}'.format(REFERENCE_PATH, img))
            reference = cv2.imread('{}\{}'.format(REFERENCE_PATH, img))

    # initializes webcam
    webcam = cv2.VideoCapture(0)

    use_this_frame = True
    while True:
        # process alternate frames
        if not use_this_frame:
            use_this_frame = True
            continue

        # gets frame from webcam
        ret, image = webcam.read()
        while not ret:
            ret, image = webcam.read()

        # compares reference image with new image
        if compare(image, reference):
            # closes webcam and goes to login function
            webcam.release()
            login()
            return

        use_this_frame = False

    return


if __name__ == '__main__':
    main()
