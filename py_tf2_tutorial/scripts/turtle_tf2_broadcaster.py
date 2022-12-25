#!/usr/bin/env python3

import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    # tf requires broadbaster
    # Be Careful, !!TF IS NOT A TOPIC!!
    br = tf2_ros.TransformBroadcaster()

    # prepare tf msg
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    # Experiment, Late tf2
    # t.header.stamp = rospy.Time.now() - rospy.Duration(60)
    t.header.frame_id = "world"
    
    t.child_frame_id = turtlename
    
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0
    
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    # copy the information from the 3D turtle pose into the 3D transform.
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    turtlename = rospy.get_param('~turtle', 'turtle1')
    # turtlename = 'turtle1'

    # The node subscribes to topic "turtleX/pose" 
    # and runs function handle_turtle_pose on every incoming message.
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()