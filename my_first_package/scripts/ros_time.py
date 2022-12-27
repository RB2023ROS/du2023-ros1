#!/usr/bin/env python3

import rospy

class TimeExample:

    def __init__(self):
        self.counter_ = 0
        self.timer_ = rospy.Timer(rospy.Duration(100.0/100.0), self.hello_du)

    def hello_du(self, event=None):
        
        now  = rospy.Time.now()
        seconds = now.to_sec()

        rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
        rospy.loginfo("Current time to_sec %i", seconds)

        delta = rospy.Duration(0.5)
        past  = now - delta
        rospy.loginfo("Past time %i %i", past.secs, past.nsecs)

def rospy_time_ex():
    rospy.init_node('rospy_time_ex', anonymous=True)

    time_ex = TimeExample()

    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        time_ex.hello_du()
        r.sleep()

if __name__ == '__main__':
    try:
        rospy_time_ex()
    except rospy.ROSInterruptException:
        pass