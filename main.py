import cv2
import numpy as np

import telebot

bot = telebot.TeleBot("1415410782:AAGWJDAfP_tgTVcgFwOFx6Um7a5ilhGzmU8")
chat = 776882021

wc = True


cam = cv2.VideoCapture("sample-mp4-file.mp4")
prev = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
def difference(prev,current):
    return np.count_nonzero(np.array(np.ravel(cv2.absdiff(prev,current))))

face = cv2.CascadeClassifier("face.xml")

original = cam.read()[1]
current = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)

while 1:
    delta = difference(current,prev)

    if delta > 20000:
        faces = face.detectMultiScale(current)

        if len(faces):
            for (x,y,w,h) in faces:
                cv2.rectangle(original,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow("",original)
            if wc:
                cv2.imwrite("kek.png",original)
                bot.send_photo(chat,open("kek.png",'rb'))
            FPS = 60
            key = cv2.waitKey(int(1000/FPS))
            if key == 27:
                break

    prev = current
    original = cam.read()[1]
    current = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

