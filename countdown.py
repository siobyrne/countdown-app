#! python3
# countdown.py - get user defined timeframe and count down

import time, subprocess

def countdown():
    print("Enter your time in seconds.")
    
    timeLeft = int(input("> "))
    
    while timeLeft > 0:
        print(timeLeft, end='')
        time.sleep(1)
        timeLeft = timeLeft - 1
        
        # when countdown ends, sound alarm
        subprocess.Popen(['open', 'alarm.wav'])
        
countdown()
