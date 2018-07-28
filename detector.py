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
from processing import find_mask, find_contours, get_main_contour, get_approx_shape, get_convex_hull 
from drawing import draw_contours
from positioning import Polygon, PointInPolygon, Point, create_polygon_from_contours

# Read an image from disk
# @param {path} the path of the image to read
# @returns {image} the image
def read_image(path):
    return cv.imread(path)

# @param {image} image to draw on
# @param {Polygon} a polygon build from many [x, y] points
# @param {int=50} the size of the squares in pixels
def draw_grid(image, poly, color, step=50):
    x = 0
    y = 0
    height = len(image)
    width = len(image[0])

    while y < height:
        while x < width:
            upper_left = Point(x, y)
            upper_right = Point(x + step, y)
            lower_left = Point(x, step + y)
            lower_right = Point(x + step, y + step)

            # only draw if the all four points of the square
            # would be inside the polygon (the Lake)
            if PointInPolygon(poly, upper_left) \
               and PointInPolygon(poly, upper_right) \
               and PointInPolygon(poly, lower_left) \
               and PointInPolygon(poly, lower_right):
                
                # top line
                cv.line(image, (x, y), (x + step, y), color, 1, 1)
                # bottom line
                cv.line(image, (x, step + y), (x + step, step + y), color, 1, 1)
                # left line
                cv.line(image, (x, y), (x, step + y), color, 1, 1)
                # right line
                cv.line(image, (x + step, y), (x + step, step + y), color, 1, 1)
            else:
                pass

            x += step
        x = 0
        y += step
        
def draw_contours_and_grid_by_algorithm(algorithm, filename, color, fig_name):
    # Color of a lake [blue green red]
    BGR = np.array([255, 218, 170])
    upper = BGR + 10
    lower = BGR - 10

    # get outline (contour) lines of Lake
    image = read_image(filename)
    mask = find_mask(image, lower, upper)
    contours = find_contours(mask)
    main_contour = get_main_contour(contours) 

    #hull = get_convex_hull(main_contour)
    the_contours = algorithm(main_contour)

    draw_contours([the_contours], image, color)

    approx_poly = create_polygon_from_contours(the_contours)
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

