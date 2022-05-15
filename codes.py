import RPi.GPIO as GPIO
import time
import datetime

nem_sensoru = 40
motor = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(nem_sensoru,GPIO.IN)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)

zaman=""

while True:
    x = GPIO.input(40)
    print(x)
    if x==0:
        GPIO.output(7,True)
        GPIO.output(32,True)

    else:
        GPIO.output(7,False)
        GPIO.output(32,False)
        GPIO.output(37,True)
        time.sleep(0.4)
        GPIO.output(37,False)
        zaman=datetime.datetime.now()
        dosya=str(zaman.day)+"-"+str(zaman.month)+"-"+str(zaman.year)+".txt"
        f=open(dosya,"a")
        f.write("\n")
        f.write(str(zaman.day)+"."+str(zaman.month)+"."+str(zaman.year)+"tarihinde"+str(zaman.hour)+":"+str(zaman.minute)+":"+str(zaman.second)+"saatinde motor calismistir.")
        f.write("\n")
        f.write("-"*60)
    time.sleep(1)