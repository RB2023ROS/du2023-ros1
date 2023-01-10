#include <fstream> // ros.h doesn't contain this lib
#include <ros/ros.h>
#include <ros/package.h>
#include <geometry_msgs/Pose.h>
#include <gazebo_msgs/SpawnModel.h>


void addXml(gazebo_msgs::SpawnModel& model_in, const std::string& file_path ){
    std::ifstream file(file_path);
    std::string line;

    while (!file.eof()){
        std::getline(file, line);
        model_in.request.model_xml += line;
    }
    file.close();
}

class SpawnModelClient {
private:
    ros::ServiceClient spawn_model_prox;

    int model_num_ = 0;
    double theta_  = 0.0;
public:
    SpawnModelClient(ros::NodeHandle *nh){
        spawn_model_prox = nh->serviceClient<gazebo_msgs::SpawnModel>("gazebo/spawn_urdf_model");

        for(auto i = 0; i < 100; i++){
            this->serviceCall();
        }
    }

    void serviceCall(){

        gazebo_msgs::SpawnModel model;

        // add roslib in find_package()
        auto file_path = ros::package::getPath("cpp_service_pkg") +  "/urdf/box.urdf";

        addXml(model, file_path);

        model.request.model_name = "box" + std::to_string(model_num_++);
        model.request.reference_frame = "world";

        model.request.initial_pose = getPose();

        // ServiceClient.call() => return bool type
        if (spawn_model_prox.call(model)){
            auto response = model.response;
            ROS_INFO("%s", response.status_message.c_str()); // Print the result given by the service called
        }
        else {
            ROS_ERROR("Failed to call service /trajectory_by_name");
            ros::shutdown();
        }

        model_num_++;
    }

    geometry_msgs::Pose getPose(){
        geometry_msgs::Pose initial_pose;

        initial_pose.position.x = theta_ * cos(theta_);
        initial_pose.position.y = theta_ * sin(theta_);
        theta_ += 0.2;
        initial_pose.position.z = 0.2;

        initial_pose.orientation.z = -0.707;
        initial_pose.orientation.w = 0.707;

        return initial_pose;
    }
};


int main(int argc, char** argv){

    ros::init(argc, argv, "gazebo_spawn_model");
    ros::NodeHandle nh;
    SpawnModelClient spawn_model_client(&nh);

    ros::shutdown();

    return 0;
}