#!/usr/bin/env python
# encoding: utf-8

import time

try:
    import importlib.util
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    # handle failed import
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(12, GPIO.HIGH)
    print("Led 1 nyala")
    time.sleep(1)
    print("Led 1 mati")
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    print("Led 2 nyala")
    time.sleep(1)
    print("Led 2 mati")
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    print("Led 3 nyala")
    time.sleep(1)
    print("Led 3 mati")
    GPIO.output(18, GPIO.LOW)
