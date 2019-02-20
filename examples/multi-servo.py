# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
# original values
#servo_min = 150  # Min pulse length out of 4096
#servo_max = 600  # Max pulse length out of 4096
# adjusted for my servos  Kuman SG80  Gold Label
#servo_min = 130
#servo_max = 550

# limit level for each servo
servo_min = [115,126,115,125,115,125]    # PWM freq = 50Hz
servo_max = [460,475,460,535,480,535]

#servo_min = [130,140,130,150,130,150]    # PWM freq = 60Hz
#servo_max = [550,560,550,630,580,630]

#servo_min = [195,210,195,220,190,205]    # PWM freq = 90Hz
#servo_max = [825,840,825,910,820,905]

#servo_min = [260,280,260,300,260,300]    # PWM freq = 120Hz
#servo_max = [1100,1120,1100,1200,1100,1200]

#servo_min = [520,560,520]    # PWM freq = 240Hz
#servo_max = [2200,2240,2200]

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)
#pwm.set_pwm_freq(60)
#pwm.set_pwm_freq(90)
#pwm.set_pwm_freq(120)
#pwm.set_pwm_freq(240)


print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    for i in range(6):
        pwm.set_pwm(i, 0, servo_min[i])
        time.sleep(0.5)
        pwm.set_pwm(i, 0, int((servo_max[i] + servo_min[i])/2))
        time.sleep(0.5)
        pwm.set_pwm(i, 0, servo_max[i])
        time.sleep(0.5)
        pwm.set_pwm(i, 0, servo_min[i])
