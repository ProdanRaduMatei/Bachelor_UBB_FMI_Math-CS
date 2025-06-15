#!/usr/bin/env python3
import rospy
import cv2
import math
import numpy as np
import time
from std_srvs.srv import Empty
from puppy_control.msg import Pose, Gait, Velocity

ROS_NODE_NAME = "move_node"

# some default values for the pose, gait and velocity
# depending on what you want to do, these values should be changed
pose_msg = Pose(roll=math.radians(0), pitch=math.radians(0), yaw=0, height=-15, x_shift=0, stance_x=0, stance_y=0, run_time=500)
gait_msg = Gait(overlap_time=0.2, swing_time=0.2, clearance_time=0.2, z_clearance=3)
vel_msg = Velocity(x=0, y=0, yaw_rate=math.radians(0))
def cleanup():
    rospy.loginfo("Shutting down...")
    # when closing, reset the servos
    rospy.ServiceProxy("/puppy_control/go_home", Empty)()

if __name__ == "__main__":
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.INFO)
    rospy.on_shutdown(cleanup)
    # first reset the servos
    rospy.ServiceProxy("/puppy_control/go_home", Empty)()
    pose_pub = rospy.Publisher("/puppy_control/pose", Pose, queue_size=1)
    gait_pub = rospy.Publisher("/puppy_control/gait", Gait, queue_size=1)
    vel_pub = rospy.Publisher("/puppy_control/velocity", Velocity, queue_size=1)

    # set the gait
    # this will remain at this value until a new gait type is specified
    gait_pub.publish(gait_msg)
    time.sleep(0.2)
    i = 0
    # set the pose
    # similar to the gait, the pose is set and will remain like this until specified otherwise
    pose_pub.publish(pose_msg)
    time.sleep(0.2)
    while not rospy.is_shutdown():
        # let the robot run for 10 steps (this was done at the lecture because the amount of space was limited)
        # normally, we don't need to count our steps but estimate how close we are to our target
        i = i + 1
        if i < 10:
            # x axis is forward or backward movement (positive for forward)
            vel_msg.x = 10
            # yaw rate is for steering to the left or right (positive for left)
            vel_msg.yaw_rate = math.radians(10)
        else:
            vel_msg.x = 0
            vel_msg.yaw_rate = 0
        vel_pub.publish(vel_msg)
        # wait for 1 second
        time.sleep(1)
