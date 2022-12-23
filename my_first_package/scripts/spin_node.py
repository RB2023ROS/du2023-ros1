#!/usr/bin/env python3

import rospy

# callback method requires event, which is TimerEvent
def hello_du(event=None):
    hello_du = "hello du %s" % rospy.get_time()
    rospy.loginfo(hello_du)

def my_first_node():
    rospy.init_node('my_first_node', anonymous=True)
    
    # Timer Class is kind of Thread.
    # It's rule is execute sleep in certain period with given event.
    rospy.Timer(rospy.Duration(1.0/100.0), hello_du)
    rospy.spin()

if __name__ == '__main__':
    try:
        my_first_node()
    except rospy.ROSInterruptException:
        pass