import cv2 as cv
from positioning import Point, point_in_polygon
# draw contours on an image
# @param {list[[int, int]]} an array of [int, int] points to draw
# @param {image} the image to draw the points on
def draw_contours(contours, image, color=(0, 0, 255)):
    cv.drawContours(image, contours, -1, color, 2)

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
            if point_in_polygon(poly, upper_left) \
               and point_in_polygon(poly, upper_right) \
               and point_in_polygon(poly, lower_left) \
               and point_in_polygon(poly, lower_right):
                
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
