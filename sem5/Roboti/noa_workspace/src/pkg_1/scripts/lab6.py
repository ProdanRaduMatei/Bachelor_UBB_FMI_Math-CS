#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from puppy_control.msg import Pose, Velocity

ROS_NODE_NAME = "image_following_node"

# Define color range for detection
COLOR_LOWER = np.array([0, 0, 135])  # lower bound for LAB color
COLOR_UPPER = np.array([255, 110, 255])  # upper bound for LAB color

# Define publishers
pose_pub = None
vel_pub = None

# Define robot messages
pose_msg = Pose(roll=0, pitch=0, yaw=0, height=-10, x_shift=0, stance_x=0, stance_y=0, run_time=500)
vel_msg = Velocity(x=0, y=0, yaw_rate=0)

# State to track ball information
ball_info = {"center_x": None, "center_y": None, "area": None, "detected": False}

def img_process(img):
    global ball_info

    # Convert ROS Image message to OpenCV image
    frame = np.ndarray(shape=(img.height, img.width, 3), dtype=np.uint8, buffer=img.data)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    lab_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    # Mask for the specified color
    mask = cv2.inRange(lab_frame, COLOR_LOWER, COLOR_UPPER)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(largest_contour) > 100:
            # Bounding box for the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)
            center_x = x + w // 2
            center_y = y + h // 2
            area = w * h  # Approximate the area of the ball

            # Draw bounding box and contour
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.drawContours(frame, [largest_contour], -1, (0, 255, 255), 2)

            # Update ball information
            ball_info.update({
                "center_x": center_x,
                "center_y": center_y,
                "area": area,
                "detected": True,
            })
        else:
            ball_info.update({"detected": False})
    else:
        ball_info.update({"detected": False})

    # Display the processed frames
    cv2.imshow("Processed mask", mask)
    cv2.imshow("Processed frame", frame)
    cv2.waitKey(1)

    # Call movement logic
    process_movement()

def process_movement():
    global ball_info, pose_pub, vel_pub, pose_msg, vel_msg

    # Movement and pitch adjustment based on ball detection
    if ball_info["detected"]:
        center_x = ball_info["center_x"]
        center_y = ball_info["center_y"]
        area = ball_info["area"]

        # Adjust pitch based on vertical ball position
        if center_y is not None:
            if center_y < 240 - 10:  # Ball is moving up
                pose_msg.pitch = max(pose_msg.pitch - 0.1, -0.5)  # Look up, bigger adjustment
                vel_msg.x = 0  # Stop backward motion while adjusting pitch
                rospy.loginfo("Ball moving up, adjusting pitch up.")
            elif center_y > 240 + 10:  # Ball is moving down
                pose_msg.pitch = min(pose_msg.pitch + 0.1, 0.5)  # Look down, bigger adjustment
                vel_msg.x = 0  # Stop backward motion while adjusting pitch
                rospy.loginfo("Ball moving down, adjusting pitch down.")
            else:
                pose_msg.pitch = 0  # Keep level pitch

        # Publish the pose adjustment
        pose_pub.publish(pose_msg)

        # Backward motion when pitch is neutral
        if pose_msg.pitch == 0:
            if area < 15000:  # Ball is far, move backward
                vel_msg.x = -3  # Backward speed
                vel_msg.yaw_rate = -0.05 if center_x < 320 else 0.05  # Slower yaw rate
                rospy.loginfo("Ball detected, moving backward slowly. Area: %d", area)
            else:  # Stop if the ball is close enough
                vel_msg.x = 0
                vel_msg.yaw_rate = 0
                rospy.loginfo("Ball close enough, stopping. Area: %d", area)

            vel_pub.publish(vel_msg)
    else:
        # Stop if no ball is detected
        vel_msg.x = 0
        vel_msg.yaw_rate = 0
        pose_msg.pitch = 0
        pose_pub.publish(pose_msg)
        vel_pub.publish(vel_msg)
        rospy.loginfo("No ball detected, stopping.")

def cleanup():
    rospy.loginfo("Shutting down...")
    cv2.destroyAllWindows()
    # Stop the robot
    vel_msg.x = 0
    vel_msg.yaw_rate = 0
    pose_msg.pitch = 0
    pose_pub.publish(pose_msg)
    vel_pub.publish(vel_msg)

if __name__ == "__main__":
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.INFO)
    rospy.on_shutdown(cleanup)

    # Initialize publishers
    pose_pub = rospy.Publisher("/puppy_control/pose", Pose, queue_size=1)
    vel_pub = rospy.Publisher("/puppy_control/velocity", Velocity, queue_size=1)

    # Subscribe to camera topic
    rospy.Subscriber("/usb_cam/image_raw", Image, img_process)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
