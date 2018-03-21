#!/usr/bin/env python3
# countdown.py - get user defined timeframe and count down

import time, subprocess

def countdown():
    print("Enter your time in seconds.")
    
    timeLeft = int(input("> "))
    
    print("Starting countdown...")
    
    while timeLeft > 0:
        print(timeLeft, end='')
        time.sleep(1)
        timeLeft = timeLeft - 1
        
        # when countdown ends, sound alarm
        subprocess.Popen(['open', 'alarm.wav'])
        
countdown()
