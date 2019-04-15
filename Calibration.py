###For more information about camer calibration and original calibration
###code please visit: https://docs.opencv.org/3.4.3/dc/dbb/tutorial_py_calibration.html

import sys
import cv2 as cv
import os
import numpy as np
import glob
import matplotlib.pyplot as plt
import pickle

############################################ VIDEO FRAME SPLIT ############################################
video_path = sys.argv[1]
images_path = "video_frames"
vidcap = cv.VideoCapture(video_path)
success,image = vidcap.read()
count = 0
success = True

try:  
    os.mkdir(images_path)
except OSError:  
    print ("Creation of the directory %s failed" % images_path)
else:  
    print ("Successfully created the directory %s " % images_path)

print ("Initializing video to frame split")

while success:
  cv.imwrite(images_path + "/frame_%d.jpg" % count, image)   
  success,image = vidcap.read()
  count += 1
print ("Video split successful")




############################################ CALIBRATION ############################################
print ("initializing camera calibration")

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
a = 6
b = 8
objp = np.zeros((a*b,3), np.float32)
objp[:,:2] = np.mgrid[0:b,0:a].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob(images_path + "/*.jpg")
for fname in images:
    print (fname + " - Processing")
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (b,a), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        print (fname + " - Accepted")
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
cv.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print ("\nCamera matrix:")
print ("fx: " + str(mtx[0][0]))
print ("fy: " + str(mtx[1][1]))
print ("cx: " + str(mtx[0][2]))
print ("cy: " + str(mtx[1][2]))

print ("\nDistortion coefficients:")
print ("k1: " + str(dist[0][0]))
print ("k2: " + str(dist[0][1]))
print ("p1: " + str(dist[0][2]))
print ("p2: " + str(dist[0][3]))
print ("k3: " + str(dist[0][4]))
