import Adafruit_PCA9685
import time

    
class servo_Class:
    #"Channel" is the channel for the servo motor on PCA9685
    #"ZeroOffset" is a parameter for adjusting the reference position of the servo motor
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset

        #Initialize Adafruit_PCA9685
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(int(60))

    # Angle setting
    def SetPos(self,pos):
        #PCA9685 controls angles with pulses, 150~650 of pulses correspond to 0~180° of angle
        pulse = int((650-150)/180*pos+150+self.ZeroOffset)
        self.pwm.set_pwm(self.Channel, 0, pulse)

    # End processing
    def Cleanup(self):
        #The servo motor is set at 90°.
        self.SetPos(int(0))
        print('0')
##############################Servo Ends Here###################

Servo0 = servo_Class(Channel=0, ZeroOffset=0)
Servo1 = servo_Class(Channel=3, ZeroOffset=0)
Servo2 = servo_Class(Channel=7, ZeroOffset=0)
Servo3 = servo_Class(Channel=5, ZeroOffset=0)

Color = 'up'
print('Fruit detected at '+Color)

########################open
deg = 180
while True:
    deg = deg - 1
    Servo0.SetPos(int(deg))
    print(deg)
    time.sleep(0.01)
    if deg <= 0:
        break
####################front

for deg in range(180):
    Servo1.SetPos(int(deg))
    print(deg)
    time.sleep(0.01)

time.sleep(1)

if Color != 'down':
    ##############up
    for deg in range(360):
        Servo2.SetPos(int(deg))
        print(deg)
        time.sleep(0.01)

    time.sleep(1)

#################close
for deg in range(180):
    Servo0.SetPos(int(deg))
    print(deg)
    time.sleep(0.01)
    
time.sleep(1)

########################back

deg = 180
while True:
    deg = deg - 1
    Servo1.SetPos(int(deg))
    #print(deg)
    time.sleep(0.01)
    if deg <= 0:
        break
    
time.sleep(1)

if Color != 'down':
    #############down
    deg = 360
    while True:
        deg = deg - 1
        Servo2.SetPos(int(deg))
        #print(deg)
        time.sleep(0.01)
        if deg <= 0:
            print('ggggg')
            break

#################right
deg = 180
while True:
    deg = deg - 1
    Servo3.SetPos(int(deg))
    print(deg)
    time.sleep(0.01)
    if deg <= 90:
        break
    
########################open
deg = 180
while True:
    deg = deg - 1
    Servo0.SetPos(int(deg))
    print(deg)
    time.sleep(0.01)
    if deg <= 0:
        break

#################close
for deg in range(180):
    Servo0.SetPos(int(deg))
    print(deg)
    time.sleep(0.01)
    
time.sleep(1)

############################left
for deg in range(89, 181):
    Servo3.SetPos(int(deg))
    print(deg)
    time.sleep(0.01)