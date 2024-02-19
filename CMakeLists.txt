cmake_minimum_required(VERSION 2.8.3)
project(rospy_facedetect)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs)

# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
catkin_install_python(PROGRAMS
  ros_facedetect.py
  ros_facedetect_listener.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rospy_facedetect
)
install(FILES
  facedetect.launch
  haarcascade_frontalface_alt.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rospy_facedetect
)

