import subprocess
import yaml
import rosbag   # source /opt/ros/noetic/setup.bash
import cv2
from cv_bridge import CvBridge
import numpy as np


FILENAME = 'test'                                        # rosbag file name without .bag
ROOT_DIR = '/home/sadik/noetic_ws'                        # rosbag path
BAGFILE = ROOT_DIR + '/' + FILENAME + '.bag'
f = open(ROOT_DIR + FILENAME + '-' + 'timestamps.txt', 'w')    # for saving timestamps
if __name__ == '__main__':
    bag = rosbag.Bag(BAGFILE)
    TOPIC = '/usb_cam/image_raw'                        # image topic
    image_topic = bag.read_messages(TOPIC)
    for k, b in enumerate(image_topic):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(b.message, b.message.encoding)
        cv_image.astype(np.uint8)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(ROOT_DIR + str(b.timestamp) + '.png', cv_image)
        print('saved: ' + str(b.timestamp) + '.png')
        f.write(str(b.timestamp) + '\n')

    bag.close()

    print('PROCESS COMPLETE')
