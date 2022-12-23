#!/usr/bin/env python3

import math
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class CollisionAvoidNode:

    def __init__(self):
        self.laser_sub_ = rospy.Subscriber("scan", LaserScan, self.laser_cb)
        self.cmd_vel_pub_ = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.twist_ = Twist()

    def laser_cb(self, data):
        # TODO: Prevent robot from collision
        # make your own logic to do that

        return None

def orbit_node():
    rospy.init_node('orbit_node', anonymous=True)
    col_avd_node = CollisionAvoidNode()
    rospy.spin()

if __name__ == '__main__':
    try:
        orbit_node()
    except rospy.ROSInterruptException:
        pass