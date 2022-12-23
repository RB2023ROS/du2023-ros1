#! /usr/bin/env python3

"""
referenced from programcreek
url : https://www.programcreek.com/python/example/93572/rospkg.RosPack
"""

import math
import rospy
import rospkg
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import SpawnModel

def spawn_helix():
    rospy.init_node("gazebo_spawn_model")

    # model_name
    model_name = "box"

    # model_xml
    rospack = rospkg.RosPack()
    model_path = rospack.get_path("py_service_pkg") + "/urdf/"

    with open(model_path + model_name + ".urdf", "r") as xml_file:
        model_xml = xml_file.read().replace("\n", "")

    # robot_namespace
    robot_namespace = ""

    # initial_pose
    initial_pose = Pose()
    initial_pose.position.x = 0.0
    initial_pose.position.y = -1
    initial_pose.position.z = 0.2

    # z rotation -pi/2 to Quaternion
    initial_pose.orientation.z = -0.707
    initial_pose.orientation.w = 0.707

    # reference_frame
    reference_frame = "world"
    theta = 0.0

    spawn_model_prox = rospy.ServiceProxy("gazebo/spawn_urdf_model", SpawnModel)

    for i in range(100):
        # service call
        initial_pose.position.x = theta * math.cos(theta)
        initial_pose.position.y = theta * math.sin(theta)
        theta += 0.2
        entity_name = model_name + str(i)

        result = spawn_model_prox(
            entity_name, model_xml, robot_namespace, initial_pose, reference_frame
        )

        """ result fromat
        bool success
        string status_message
        """
        rospy.loginfo(result)

if __name__ == '__main__':
    try:
        spawn_helix()
    except rospy.ROSInterruptException:
        pass