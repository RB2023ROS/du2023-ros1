#include <ros/ros.h>
#include <std_srvs/SetBool.h>
#include <geometry_msgs/Twist.h>

using SetBool = std_srvs::SetBool;

class EmergencyStopNode {
private:
    ros::ServiceServer service_;
    ros::Publisher cmd_vel_pub_;

    geometry_msgs::Twist twist_msg_;
public:
    EmergencyStopNode(ros::NodeHandle *nh){
        service_ = nh->advertiseService("emergency_stop", &EmergencyStopNode::eStopCallback, this);
        cmd_vel_pub_ = nh->advertise<geometry_msgs::Twist>("cmd_vel", 10);

        ROS_INFO_STREAM("EmergencyStopNode Started");
    }

    void moveRobot(){
        twist_msg_.linear.x = 0.5;
        twist_msg_.angular.z = 1.0;

        cmd_vel_pub_.publish(twist_msg_);
    }

    bool eStopCallback(SetBool::Request &req, SetBool::Response &res){

        if(req.data == true){
            twist_msg_.linear.x = 0.0;
            twist_msg_.angular.z = 0.0;
            cmd_vel_pub_.publish(twist_msg_);

            res.success = true;
            res.message = "Successfully Stopped";

            return true;
        } else {
            res.success = false;
            res.message = "Stop Failed";

            return false;
        }
    }
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "emergency_stop_node");
    ros::NodeHandle nh;
    EmergencyStopNode e_stop_service(&nh);

    auto start_time = ros::Time::now();
    auto cur_time   = ros::Time::now();

    while( (cur_time - start_time) < ros::Duration(3.0)){
        e_stop_service.moveRobot();
        cur_time = ros::Time::now();
    }

    ros::spin();
    ros::shutdown();

    return 0;
}