import cv2 as cv

# applies a threshold to an image based on two boundaries
# @param {image} the image to threshold
# @param {Array[int, int, int]} lower threshold in BGR
# @param {Array[int, int, int]} upper threshold in BGR
def find_mask(image, lower, upper):
    return cv.inRange(image, lower, upper)

def find_contours(mask):
    (_, cnts, hierarchy) = cv.findContours(
            mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    return cnts

def get_main_contour(image, lower, upper):
    contours = get_contours(image, lower, upper)
    copy = contours.copy()
    copy.sort(key=len, reverse=True)
    return copy[0]

def get_approx_shape(points):
    epsilon = 0.01 * cv.arcLength(points, True)
    return cv.approxPolyDP(points, epsilon, True)

def get_contours(image, lower, upper):
    mask = find_mask(image, lower, upper)
    return find_contours(mask)

def get_convex_hull(points):
    return cv.convexHull(points)
