#include <ros/ros.h>
#include <geometry_msgs/Twist.h>

class CmdVelPubNode
{
private:
    ros::Publisher cmd_vel_pub_;
    ros::Timer timer_;

    geometry_msgs::Twist twist_msg_;

public:
    CmdVelPubNode(ros::NodeHandle *nh) {
        ROS_INFO("Publisher and Subscriber initialized");
        timer_ = nh->createTimer(ros::Duration(0.1), &CmdVelPubNode::timerCallback, this);
        cmd_vel_pub_ = nh->advertise<geometry_msgs::Twist>("cmd_vel", 10);
    }

    void timerCallback(const ros::TimerEvent& event){

        twist_msg_.linear.x = 0.5;
        twist_msg_.angular.z = 0.5;

        cmd_vel_pub_.publish(twist_msg_);
    }
};

int main(int argv, char** argc) {
    
    ros::init(argv, argc, "cmd_vel_node");
    // ros::NodeHandle nh("my_namespace");
    ros::NodeHandle nh;
    
    CmdVelPubNode cmd_pub_node(&nh);
    
    ros::spin();

    return 0;
}