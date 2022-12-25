#!/usr/bin/env python3

import rospy

class LevelNode:

    def __init__(self):
        self.counter_ = 0
        self.timer_ = rospy.Timer(rospy.Duration(100.0/100.0), self.hello_du)

    def hello_du(self, event=None):
        hello_du = f"hello du {rospy.get_time()}, counter: {self.counter_}"
        rospy.logdebug(hello_du)
        rospy.loginfo(hello_du)
        rospy.logwarn(hello_du)
        rospy.logerr(hello_du)
        rospy.logfatal(hello_du)
        self.counter_ += 1

def logger_level():
    rospy.init_node('logger_level', anonymous=True)

    oop_node = LevelNode()

    rospy.spin()

if __name__ == '__main__':
    try:
        logger_level()
    except rospy.ROSInterruptException:
        pass