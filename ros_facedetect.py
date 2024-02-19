import rospy
from std_msgs.msg import String
import cv2
import os

def face_detect():
    pub = rospy.Publisher('facedetect', String, queue_size=10)
    rospy.init_node('facedetect', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # Load the cascade
    model_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_alt.xml')
    face_cascade = cv2.CascadeClassifier(model_path)

    # Initialize the video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        rospy.logerr("Error: Unable to open camera.")
        return

    t1 = rospy.get_time()
    while not rospy.is_shutdown():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            if len(faces) > 0:
                rospy.loginfo('face detected: %s, started %s took %s' % (str(faces), t1, rospy.get_time() - t1))
                x = str(faces)[2:6]
                pub.publish(x)

        rate.sleep()

    # Release the capture
    cap.release()

if __name__ == '__main__':
    try:
        face_detect()
    except rospy.ROSInterruptException:
        pass
