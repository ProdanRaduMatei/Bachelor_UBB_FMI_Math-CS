#!/usr/bin/env python3
import rospy
ROS_NODE_NAME = "my_ros_node"
def cleanup():
	rospy.loginfo("Shutting down...")
if __name__ == '__main__':
	rospy.init_node(ROS_NODE_NAME, log_level = rospy.INFO)
	rospy.on_shutdown(cleanup)
