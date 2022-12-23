#! /usr/bin/env python3

import rospy
from roslaunch.pmon import start_process_monitor

from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool, SetBoolResponse

class EmergencyStopNode(object):

    def __init__(self):
        self.cmd_vel_pub_ = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.stop_server_ = rospy.Service("emergency_stop", SetBool, self.stop_cb)
        
        self.pm_ = start_process_monitor()
        self.twist_msg_   = Twist()
        self.response_    = SetBoolResponse()

        rospy.loginfo("E Stop Server Started")
        
        self.twist_pub()
        rospy.sleep(0.1)
    
    def twist_pub(self):
        self.twist_msg_.linear.x  = 0.5
        self.twist_msg_.angular.z = 1.0

        self.cmd_vel_pub_.publish(self.twist_msg_)
    
    def stop_cb(self, request):
        
        if request.data is True:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = 0.0
            self.cmd_vel_pub_.publish(self.twist_msg_)

            self.response_.success = True
            self.response_.message = "Successfully Stopped"
        else:
            self.response_.success = False
            self.response_.message = "Stop Failed"

        return self.response_

def main():
    rospy.init_node("emergency_stop_node")
    
    e_stop_node = EmergencyStopNode()
    rospy.sleep(1.0)
    e_stop_node.twist_pub()

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass