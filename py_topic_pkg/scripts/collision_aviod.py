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

        left_side_count = 0
        right_side_count = 0
        
        for i, point in enumerate(data.ranges):
            if not math.isinf(point) and point < 1.0:
                if i > 180:
                    left_side_count += 1
                else:
                    right_side_count += 1
                    
        self.twist_.linear.x = 0.3
        self.twist_.angular.z = (right_side_count - left_side_count) / 100

        self.cmd_vel_pub_.publish(self.twist_)

def orbit_node():
    rospy.init_node('orbit_node', anonymous=True)
    col_avd_node = CollisionAvoidNode()
    rospy.spin()

if __name__ == '__main__':
    try:
        orbit_node()
    except rospy.ROSInterruptException:
        pass