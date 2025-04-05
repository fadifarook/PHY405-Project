# PHY405-Project
Code for Generating two-signal, and modifying the pwm carrier frequency of Arduino.

This is part of a project where audio is transmitted through  a laser diode over a distance. There are two files included in this repository that support the project.

## 1. twotone.py
This python script uses scipy.io.wavfile module to generate a 25Hz + 50Hz two tone audio signal for testing. It is output into a wav file. A plot of the first two cycles is also generated.

## 2. ADC_20kHz.ino
This arduino script requires the TimerOne library (https://github.com/PaulStoffregen/TimerOne). 

It involves reading an input analog audio signal, and updating the duty cycle of the PWM pulse at 10kHz frequency. The carrier frequency of the PWM signal is 20KHz (requires the library change from default frequency).
