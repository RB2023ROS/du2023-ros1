#! /usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist
from custom_interfaces.srv import QuadrotorControl, QuadrotorControlResponse

class QuadRotorUpDown(object):

    def __init__(self):
        self.cmd_vel_pub_ = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.stop_server_ = rospy.Service("up_down", QuadrotorControl, self.up_down_cb)
        
        self.twist_msg_   = Twist()
        self.response_    = QuadrotorControlResponse()

        rospy.loginfo("Quadrotor Up-Down Server Started")
    
    def up_down_cb(self, request):

        if request.command == "land":
            self.twist_msg_.linear.z  = -0.5
            self.response_.success = True
        elif request.command == "takeoff":
            self.twist_msg_.linear.z  = 0.5
            self.response_.success = True
        else:
            rospy.logwarn("Unknown Command")
            self.response_.success = False
            return self.response_

        start = rospy.Time.now()
        now = rospy.Time.now()
        while (now - start).secs < request.seconds:
            now = rospy.Time.now()
            self.cmd_vel_pub_.publish(self.twist_msg_)
        
        rospy.loginfo(f"{request.command} done, quadrotor stop")
        self.twist_msg_.linear.z = 0.0
        self.cmd_vel_pub_.publish(self.twist_msg_)

        return self.response_

def main():
    rospy.init_node("emergency_stop_node")
    
    q_up_down = QuadRotorUpDown()

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass