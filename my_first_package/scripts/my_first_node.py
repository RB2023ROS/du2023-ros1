#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def my_first_node():
    # ROS nodes require initialization
    # It contains master registration, uploading parameters
    rospy.init_node('my_first_node', anonymous=True)
    
    # ROS safe timer
    rate = rospy.Rate(10) # 10hz
    
    # Loop control Example
    while not rospy.is_shutdown():
        hello_du = "hello du %s" % rospy.get_time()
        rospy.loginfo(hello_du)
        # Below line calls sleep method in Python internally.
        rate.sleep()

if __name__ == '__main__':
    try:
        my_first_node()
    except rospy.ROSInterruptException:
        pass