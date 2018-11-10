#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Joy, Imu
import numpy as np

angular_velocity_covariance = np.diag([0.01, 0.01, 0.01]).reshape([9]).tolist()
linear_acceleration_covariance = np.diag([0.01, 0.01, 0.01]).reshape([9]).tolist()

ros2radps = -0.55849
ros2mps2 = -39.199

def callback(joy):
	imu = Imu()
	imu.orientation_covariance[0] = -1
	imu.angular_velocity_covariance = angular_velocity_covariance
	imu.angular_velocity.x = joy.axes[13] * ros2radps
	imu.angular_velocity.y = joy.axes[11] * ros2radps
	imu.angular_velocity.z = joy.axes[12] * ros2radps
	imu.linear_acceleration_covariance = linear_acceleration_covariance
	imu.linear_acceleration.x = joy.axes[6] * ros2mps2
	imu.linear_acceleration.y = joy.axes[7] * ros2mps2
	imu.linear_acceleration.z = joy.axes[8] * ros2mps2
	pub.publish(imu)

rospy.init_node('ds4', anonymous = True)
pub = rospy.Publisher('ds4/imu', Imu, queue_size = 20)
rospy.Subscriber('/joy', Joy, callback)
rospy.spin()
