#!usr/bin/env python3
import rospy
ROS_NODE_NAME="my_ros_node"
def workFunction():
	rate=rospy.Rate(1)
	while not rospy.is_shutdown():
		rospy.loginfo("test")
		rate.sleep()
def cleanup():
	rospy.loginfo("Shutting down...")
if __name__=='__main__':
	rospy.init_node(ROS_NODE_NAME, log_level=rospy.INFO)
	rospy.on_shutdown(cleanup)
	try:
		workFunction()
	except KeyboardInterrupt:
		pass
