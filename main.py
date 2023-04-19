# To find point to point distances
from scipy.spatial import distance as dist 
from imutils.video import VideoStream
 # For image processing on images
from imutils import face_utils
from threading import Thread # For multi-threading
import dlib  # For face landmark detection
import cv2 # For enabling computer vision
import imutils
import numpy as np
from pygame import mixer
import time
import os
from playsound import playsound