##
# Code to detect lakes from Google Maps Images
# By Lachlan Miller
# github.com/lmiller1990

# Reference: 
# https://www.pyimagesearch.com/2014/10/20/finding-shapes-images-using-python-opencv/
##

import cv2 as cv
import numpy as np
from raycast_test import Polygon, PointInPolygon, Point

# Color of a lake [blue green red]
BGR = np.array([255, 218, 170])
upper = BGR + 10
lower = BGR - 10

# Read an image from disk
# @param {path} the path of the image to read
# @returns {image} the image
def read_image(path):
    return cv.imread(path)

# applies a threshold to an image based on two boundaries
# @param {image} the image to threshold
# @param {Array[int, int, int]} lower threshold in BGR
# @param {Array[int, int, int]} upper threshold in BGR
def find_mask(image):
    return cv.inRange(image, lower, upper)

def find_contours(mask):
    (_, cnts, hierarchy) = cv.findContours(
            mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    print("Found %d black shapes" % (len(cnts)))
    return cnts

# draw contours on an image
# @param {list[[int, int]]} an array of [int, int] points to draw
# @param {image} the image to draw the points on
def show_contours(contours, image):
    cv.drawContours(image, contours, -1, (0, 0, 255), 2)

    cv.imshow("contours", image)

def draw_grid(image, step=50):
    x = 0
    y = 0
    height = len(image)
    width = len(image[0])

    while y < height:
        while x < width:
            # horizontal lines
            cv.line(image, (x, 0), (x + step, 0), (255, 0, 0), 1, 1)
            cv.line(image, (x, step), (x + step, step), (255, 0, 0), 1, 1)

            cv.line(image, (x, 0), (x, step), (255, 0, 0), 1, 1)
            cv.line(image, (x + step, 0), (x + step, step), (255, 0, 0), 1, 1)
            x += step
        y += step
    

def calculate_midpoint(contours):
    x = 0
    y = 0
    for c in contours:
        x += c[0]
        y += c[1]

    return [x / len(contours), y / len(contours)]

def get_main_contour(contours):
    copy = contours.copy()
    copy.sort(key=len, reverse=True)
    return copy[0]

if __name__ == "__main__":
    image = read_image("pond.png")
    mask = find_mask(image)

    contours = find_contours(mask)
    main_contour = get_main_contour(contours) 
    draw_grid(image)
    show_contours([main_contour], image)
    print(len(image), len(image[0]))

    key = cv.waitKey(0)

