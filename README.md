
# Modified for PCA9685 compatible control board and SG90 compatible servo motors.

RPi   |PCA9685|ext |
------|:-----:|----|
\---  |V+     |5V  |
3.3V  |VCC    |    |
GPIO2 |SDA    ||
GPIO3 |SCL    ||
GPIO4 |OE     ||
GND   |GND    |GND|

# min and max of pulse at PWM Frequency 60Hz
130 - 550 / 4096

周波数をあげた方がシャキッと動くが、あまり高くできないモノもある。可動域、max側が狭まる感じ？
min, maxの範囲外になると振動が激しくなる。180度回転させなくていいのなら、可動域を狭めにしてPWM周波数をあげると良いかな。

python3 examples/multi-servo.py


# Adafruit Python PCA9685
Python code to use the PCA9685 PWM servo/LED controller with a Raspberry Pi or BeagleBone black.

## Installation

To install the library from source (recommended) run the following commands on a Raspberry Pi or other Debian-based OS system:

    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
    cd Adafruit_Python_PCA9685
    sudo python setup.py install

Alternatively you can install from pip with:

    sudo pip install adafruit-pca9685

Note that the pip install method **won't** install the example code.
