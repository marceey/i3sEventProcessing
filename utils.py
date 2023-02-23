import cv2
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt


def quadratic_crop_event(event, newsize):
    """
    This function takes an event and new size as inputs, and returns the event after cropping the area around the
    center point defined by (320, 240) with a quadratic shape of size newsize.
    """
    event = event[(event[:, 0] < (320 + newsize/2)) & (event[:, 0] > (320 - newsize/2)) &
                  (event[:, 1] < (240 + newsize/2)) & (event[:, 1] > (240 - newsize/2))]
    return event

def timestamp_crop(event, first_timestamp, last_timestamp):
    """
    This function takes an event, the first and last timestamps as inputs,
    and returns the event after cropping it between the specified timestamps.
    """
    event = event[(event[:, 3] > first_timestamp) & (event[:, 3] < last_timestamp)]
    return event


def scatterplot_event(event):
    """
    This function takes an event as input and generates a scatter plot of the event points.
    The points in the scqtter plot are colored red if their polarity is 1 (positive)
    and blue if their polarity is 0 (negative). The plot is displayed and saved as a file named "example".
    """
    event = event.T
    fig_anim = plt.figure(figsize=(12, 12))
    plt.scatter(y=-event[1], x=event[0], s=0.5, color=np.where(event[2], 'r', 'C0'))
    plt.show()
    plt.savefig('example')

def blackwhite_image(event):
    """
    This function takes an event as input and returns a black and white image representation of the event.
    It first creates an empty image with dimensions 640x480x10 and then iterates over the event points
    to add white pixels to the image at the corresponding (x,y,t) locations. The resulting image is returned.
    """
    n_frames = 10
    image = np.zeros((n_frames, 640, 480), dtype='uint8')

    im = np.zeros((640, 480, 1), dtype='uint8')
    pixels_1 = event[np.where(event[:, 2] == 0)]

    for px_1 in pixels_1:
        img = cv2.resize(im, (480, 640), interpolation=cv2.INTER_AREA)
        image = img.T
        im = Image.fromarray(image)
        im.show()

    return image

def face_landmarks(image):
    """
    This function takes an image file as input, uses the face_recognition library to detect faces in the image,
    and draws facial landmarks on the image. It prints the number of faces detected and the coordinates of the facial
    features for each detected face. The resulting image with the facial landmarks is displayed.
    """
    image = face_recognition.load_image_file(image)
    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

    # Create a PIL imagedraw object so we can draw on the picture
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)

    for face_landmarks in face_landmarks_list:

        # Print the location of each facial feature in this image
        for facial_feature in face_landmarks.keys():
            print("The {} in this face has the following points: {}".format(facial_feature,
                                                                            face_landmarks[facial_feature]))

        # Let's trace out each facial feature in the image with a line!
        for facial_feature in face_landmarks.keys():
            d.line(face_landmarks[facial_feature], width=5)

    # Show the picture
    pil_image.show()

