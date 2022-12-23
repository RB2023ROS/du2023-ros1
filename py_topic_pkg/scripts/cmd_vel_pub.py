#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class CmdVelPubNode:

    def __init__(self):
        # Publisher requires 3 paramters
        #  1. topic name
        #  2. topic msg type
        #  3. topic queue size
        self.cmd_vel_pub_ = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.timer_ = rospy.Timer(rospy.Duration(1.0/10.0), self.pub_msg)
        self.twist_ = Twist()

    def pub_msg(self, event=None):
        # geometry_msgs.Twist
        # ref: http://docs.ros.org/en/melodic/api/geometry_msgs/html/msg/Twist.html
        self.twist_.linear.x = 0.5
        self.twist_.angular.z = 1.0
        
        self.cmd_vel_pub_.publish(self.twist_)

def cmd_vel_node():
    rospy.init_node('cmd_vel_node', anonymous=True)
    cmd_vel_pub_node = CmdVelPubNode()
    rospy.spin()

if __name__ == '__main__':
    try:
        cmd_vel_node()
    except rospy.ROSInterruptException:
        pass