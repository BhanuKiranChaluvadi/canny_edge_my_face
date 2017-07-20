cmake_minimum_required(VERSION 2.8.3)
project(canny_edge_my_face)

find_package(catkin REQUIRED COMPONENTS std_msgs cv_bridge rospy roscpp)

catkin_package(CATKIN_DEPENDS std_msgs cv_camera)
