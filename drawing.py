import cv2 as cv

# draw contours on an image
# @param {list[[int, int]]} an array of [int, int] points to draw
# @param {image} the image to draw the points on
def draw_contours(contours, image, color=(0, 0, 255)):
    cv.drawContours(image, contours, -1, color, 2)
