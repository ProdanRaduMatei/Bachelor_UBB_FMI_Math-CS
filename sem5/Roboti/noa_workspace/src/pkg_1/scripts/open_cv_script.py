#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
ROS_NODE_NAME = "image_processing_node"
def img_process(img):
    rospy.loginfo("image width: %s height: %s" % (img.width, img.height))
    frame = np.ndarray(shape=(img.height, img.width, 3), dtype=np.uint8, buffer=img.data)
    cv2_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.rectangle(cv2_img, (50, 50), (200, 200), (0, 255, 0), 2)
    cv2.imshow("Frame", cv2_img)
    cv2.waitKey(1) #this forces the window opened by OpenCV to remain open
def cleanup():
    rospy.loginfo("Shutting down...")
    cv2.destroyWindow("Frame")
if __name__ == "__main__":
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.INFO)
    rospy.on_shutdown(cleanup)
    rospy.Subscriber("/usb_cam/image_raw", Image, img_process)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass