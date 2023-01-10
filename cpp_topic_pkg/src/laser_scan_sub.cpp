#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/LaserScan.h>

class LaserSubNode
{
private:
    ros::Subscriber laser_sub_;
    ros::Timer timer_;

public:
    LaserSubNode(ros::NodeHandle *nh) {
        ROS_INFO("Publisher and Subscriber initialized");
        laser_sub_ = nh->subscribe("scan", 10, &LaserSubNode::laserSubCallback, this);
    }

    void laserSubCallback(const sensor_msgs::LaserScan &data){
        
        ROS_INFO_STREAM("data.ranges[0]: " << data.ranges[0]);
        ROS_INFO_STREAM("data.ranges[90]: " << data.ranges[90]);
        ROS_INFO_STREAM("data.ranges[179]: " << data.ranges[179]);
        ROS_INFO_STREAM("data.ranges[270]: " << data.ranges[270]);
        ROS_INFO_STREAM("data.ranges[360]: " << data.ranges[360]);
        // std::cout << std::to_string(data.ranges[0]) << std::endl;

        ROS_INFO("Publisher and Subscriber initialized");

    }
};

int main(int argv, char** argc) {
    
    ros::init(argv, argc, "laser_sub_node");
    // ros::NodeHandle nh("my_namespace");
    ros::NodeHandle nh;
    
    LaserSubNode laser_sub_node(&nh);
    
    ros::spin();

    return 0;
}