#!/usr/bin/env python3

import rospy

class ParamNode:

    def __init__(self):
        self.str_param_ = rospy.get_param('~str_param', 'hello_world')
        self.int_param_ = rospy.get_param('~int_param', 2023)
        self.double_param_ = rospy.get_param('~double_param', 3.14)
        self.bool_param_ = rospy.get_param('~bool_param', True)
        self.list_of_float_param_ = rospy.get_param('~list_of_float_param', [1., 2., 3., 4.])

        rospy.loginfo(f"""
        self.str_param_ = {self.str_param_}
        self.int_param_ = {self.int_param_}
        self.double_param_ = {self.double_param_}
        self.bool_param_ = {self.bool_param_}
        self.list_of_float_param_ = {self.list_of_float_param_}
        """)

def param_node():
    rospy.init_node('param_node', anonymous=True)
    param_node = ParamNode()
    rospy.spin()

if __name__ == '__main__':
    try:
        param_node()
    except rospy.ROSInterruptException:
        pass