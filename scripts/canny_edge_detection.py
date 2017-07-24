#!/usr/bin/env python
import rospy
import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class EdgeDetection(object):
	
	def __init__(self):

		rospy.init_node('edge_detection')

		self.bridge = CvBridge()

		rospy.Subscriber('/webcam/image_raw', Image, self.image_callback)

		rospy.spin()

	def image_callback(self, msg):

		try:
			# Convert your ROS image into OPENCV2
			cv2_img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
			# Appl canny edges
			edges = cv2.Canny(cv2_img,100,200)
			cv2.imshow('Edges', edges)
			cv2.waitKey(3)
		except CVBridgeError, e:
			print(e) 
			raise e


if __name__ == '__main__':

	detector = EdgeDetection()
