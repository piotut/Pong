import numpy as np
import cv2
import Tkinter
import threading


class Strojnik(object):
    def __init__(self):
        self.hsv = {
            'MAX_S': 0,
            'MIN_S': 0,
            'MAX_H': 0,
            'MIN_H': 0,
            'MAX_V': 0,
            'MIN_V': 0
        }
        self.wh = Tkinter.Tk()

    def to_file(self, filename, value=[]):
        with open(filename, 'w') as fileh:
            fileh.write(';'.join([str(x) for x in value]))

    def change_value(self, key, value):
        self.hsv[key] = value

    def scroll(self):

        l1 = Tkinter.LabelFrame(self.wh, text='min_s')
        l2 = Tkinter.LabelFrame(self.wh, text='min_v')
        l3 = Tkinter.LabelFrame(self.wh, text='min_h')
        l4 = Tkinter.LabelFrame(self.wh, text='max_s')
        l5 = Tkinter.LabelFrame(self.wh, text='max_v')
        l6 = Tkinter.LabelFrame(self.wh, text='max_h')
        s1 = Tkinter.Scale(
                l1,
                orient=Tkinter.HORIZONTAL, 
                command=lambda x: self.change_value('MIN_S', s1.get()),
                to = 500
            )
        s2 = Tkinter.Scale(
                l2,
                orient=Tkinter.HORIZONTAL, 
                command=lambda x: self.change_value('MIN_V', s2.get()),
                to = 500
            )
        s3 = Tkinter.Scale(
                l3,
                orient=Tkinter.HORIZONTAL, 
                command=lambda x: self.change_value('MIN_H', s3.get()),
                to = 500
            )
        s4 = Tkinter.Scale(
                l4,
                orient=Tkinter.HORIZONTAL, 
                command=lambda x: self.change_value('MAX_S', s4.get()),
                to = 500
            )
        s5 = Tkinter.Scale(
                l5,
                orient=Tkinter.HORIZONTAL, 
                command=lambda x: self.change_value('MAX_V', s5.get()),
                to = 500
            )
        s6 = Tkinter.Scale(
                l6,
                orient=Tkinter.HORIZONTAL, 
                command=lambda x: self.change_value('MAX_H', s6.get()),
                to = 500
            )

        lfile = Tkinter.Label(self.wh, text="Filename")
        lfile.pack()
        entry = Tkinter.Entry(self.wh, bd =5)
        entry.pack()

        save_button = Tkinter.Button(
                self.wh,
                text = 'save to file',
                command=lambda: self.to_file(entry.get(), [s3.get(), s1.get(), s2.get(), s6.get(), s4.get(), s5.get()]),

            )

        save_button.pack()
        l1.pack(fill='x')
        l2.pack(fill='x')
        s1.pack(fill='x')
        s2.pack(fill='x')
        l3.pack(fill='x')
        l4.pack(fill='x')
        s3.pack(fill='x')
        s4.pack(fill='x')
        l5.pack(fill='x')
        l6.pack(fill='x')
        s5.pack(fill='x')
        s6.pack(fill='x')
        self.wh.mainloop()

    def run(self):

        cap = cv2.VideoCapture(1)
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        hsv_min = (self.hsv['MIN_H'], self.hsv['MIN_S'], self.hsv['MIN_V'])
        hsv_max = (self.hsv['MAX_H'], self.hsv['MAX_S'], self.hsv['MAX_V'])
        mask = cv2.inRange(hsv, hsv_min, hsv_max)

        while(1):
            ret, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            hsv_min = (self.hsv['MIN_H'], self.hsv['MIN_S'], self.hsv['MIN_V'])
            hsv_max = (self.hsv['MAX_H'], self.hsv['MAX_S'], self.hsv['MAX_V'])
            mask = cv2.inRange(hsv, hsv_min, hsv_max)

            cv2.imshow("image", frame)
            cv2.imshow("hsv", hsv)
            cv2.imshow("mask", mask)

            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break

if __name__ == "__main__":
    track = Strojnik()
    t = threading.Thread(target=track.run)
    t.start()
    track.scroll()
    t.join()
