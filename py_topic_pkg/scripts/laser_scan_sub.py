#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

class LaserSubNode:

    def __init__(self):
        # Publisher requires 3 paramters
        #  1. topic name
        #  2. topic msg type
        #  3. sub callback method
        self.laser_sub_ = rospy.Subscriber("scan", LaserScan, self.laser_cb)

    # first param of callback method is always topic msg
    def laser_cb(self, data):
        rospy.loginfo( len(data.ranges))

        print(f"""
        data.ranges[0]: {data.ranges[0]}
        data.ranges[90]: {data.ranges[90]}
        data.ranges[179]: {data.ranges[179]}
        data.ranges[270]: {data.ranges[270]}
        data.ranges[360]: {data.ranges[360]}
        """)

def laser_sub_node():
    rospy.init_node('laser_sub_node', anonymous=True)
    laser_sub_node = LaserSubNode()
    rospy.spin()

if __name__ == '__main__':
    try:
        laser_sub_node()
    except rospy.ROSInterruptException:
        pass