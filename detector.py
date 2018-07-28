##
# Code to detect lakes from Google Maps Images
# By Lachlan Miller
# github.com/lmiller1990
#
# Reference: 
# https://www.pyimagesearch.com/2014/10/20/finding-shapes-images-using-python-opencv/
##

import cv2 as cv
import numpy as np
from colors import blue, red, green
from processing import get_main_contour, get_approx_shape, get_convex_hull 
from drawing import draw_grid, draw_contours
from positioning import create_polygon_from_contours

# Read an image from disk
# @param {path} the path of the image to read
# @returns {image} the image
def read_image(path):
    return cv.imread(path)

# @param {image} image to draw on
# @param {Polygon} a polygon build from many [x, y] points
# @param {int=50} the size of the squares in pixels
        
def draw_contours_and_grid_by_algorithm(algorithm, filename, color, fig_name):
    image = read_image(filename)

    # Color of a lake [blue green red]
    BGR = np.array([255, 218, 170])
    upper = BGR + 10
    lower = BGR - 10

    # get a list of contour points around the Lake
    main_contour = get_main_contour(image, lower, upper) 

    contours = algorithm(main_contour)

    draw_contours([contours], image, color)

    approx_poly = create_polygon_from_contours(contours)
    draw_grid(image, approx_poly, color)

    cv.imshow(fig_name, image)


if __name__ == "__main__":
    # draw contour using approximate shape
    # https://docs.opencv.org/3.4.0/dd/d49/tutorial_py_contour_features.html
    # section 4
    draw_contours_and_grid_by_algorithm(
            get_approx_shape, "pond.png", blue, "Approximate")

    # draw contour using convex hull
    # https://docs.opencv.org/3.4.0/dd/d49/tutorial_py_contour_features.html
    # section 5
    draw_contours_and_grid_by_algorithm(
            get_convex_hull, "pond.png", red, "Convex Hull")

    key = cv.waitKey(0)

