#!/usr/bin/env python3

import rospy

class OOPNode:

    def __init__(self):
        self.counter_ = 0
        self.timer_ = rospy.Timer(rospy.Duration(1.0/100.0), self.hello_du)

    def hello_du(self, event=None):
        hello_du = f"hello du {rospy.get_time()}, counter: {self.counter_}"
        rospy.loginfo(hello_du)
        self.counter_ += 1

def my_first_oop_node():
    rospy.init_node('my_first_oop_node', anonymous=True)

    oop_node = OOPNode()

    rospy.spin()

if __name__ == '__main__':
    try:
        my_first_oop_node()
    except rospy.ROSInterruptException:
        pass