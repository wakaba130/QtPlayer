##
# coding:utf-8
##

import numpy as np
import cv2

class opencv_movie():
    def __init__(self):
        self.frame = 0
        self.file_name = None

    def open(self, file):
        self.file_name = file
        if self.file_name is None or type(self.file_name) != str:
            print('Error:file name is invalid.')
            return False

        self.cap = cv2.VideoCapture(self.file_name)
        if not self.cap.isOpened():
            print('Error:Video file is not Opened.')
            return False

        return True

    def load(self):
        ret, cv_img = self.cap.read()
        if not ret:
            print('Error:Video images is not loaded.')
            return None

        self.img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        return self.img

if __name__ == '__main__':
    test = opencv_movie()
    test.open('tests/sample.mp4')
    if test is None:
        exit()

    while(1):
        img = test.load()
        if img is None:
            break

        cv2.imshow('img',img)
        if cv2.waitKey(30) is 27:
            break

    cv2.destroyAllWindows()
