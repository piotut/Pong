import numpy as np
import cv2, cv
import Tkinter
import threading


class Tracking(object):
    def __init__(self, file1 = None, file2 = None):
        self.p2_hsv_min = (44, 110, 88)
        self.p2_hsv_max = (118, 316, 154)

        self.p1_hsv_min = (155, 197, 95)
        self.p1_hsv_max = (191, 268, 204)
        self.wh = Tkinter.Tk()

        if file1 and file2:
            self.read_file(file1, file2)

        self.p1_position = 250
        self.p2_position = 250

    def read_file(self, file1, file2):
        with open(file1, 'rb+') as fileh:
            hsv = fileh.read().strip()
            hsv = hsv.split(';')
            print hsv
            self.p1_hsv_min = tuple([int(x) for x in hsv[:3]])
            self.p1_hsv_max = tuple([int(x) for x in hsv[3:]])

        with open(file2, 'rb+') as fileh:
            hsv = fileh.read().strip()
            hsv = hsv.split(';')
            self.p2_hsv_min = tuple([int(x) for x in hsv[:3]])
            self.p2_hsv_max = tuple([int(x) for x in hsv[3:]])

    def run(self):

        p2_track_window = (400,250,90,90) #x, y, w, h
        p1_track_window = (100,250,90,90)

        cap = cv2.VideoCapture(1)
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        p1_mask = cv2.inRange(hsv, self.p1_hsv_min, self.p1_hsv_max)
        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
        while(1):
            ret, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # dla player1
            p1_mask = cv2.inRange(hsv, self.p1_hsv_min, self.p1_hsv_max)
            ret, p1_track_window = cv2.meanShift(p1_mask, p1_track_window, term_crit)
            x,y,w,h = p1_track_window
            self.p1_position = y
            cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)
            # dla player2
            p2_mask = cv2.inRange(hsv, self.p2_hsv_min, self.p2_hsv_max)
            ret, p2_track_window = cv2.meanShift(p2_mask, p2_track_window, term_crit)
            x,y,w,h = p2_track_window
            self.p2_position = y
            cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)

            cv2.imshow('img2',frame)
            # cv2.erode(mask, mask, None, (3, 3))
            # cv2.dilate(mask, mask, None, (8, 8))
            # cv2.imshow("image", frame)
            # cv2.imshow("hsv", hsv)
            #cv2.imshow("mask", p1_mask)
            #cv2.imshow("mask2", p2_mask)

            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break

if __name__ == "__main__":
    track = Tracking()
    track.run()
