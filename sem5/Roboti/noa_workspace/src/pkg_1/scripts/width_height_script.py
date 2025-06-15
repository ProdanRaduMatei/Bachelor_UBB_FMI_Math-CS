#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
ROS_NODE_NAME = "image_processing_node"
def img_process(img):
	rospy.loginfo("image width: %s height: %s" % (img.width, img.height))
def cleanup():
	rospy.loginfo("Shutting down...")
if __name__ == "__main__":
	rospy.init_node(ROS_NODE_NAME, log_level=rospy.INFO)
	rospy.on_shutdown(cleanup)
	rospy.Subscriber("/usb_cam/image_raw", Image, img_process)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass