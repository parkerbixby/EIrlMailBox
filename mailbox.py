import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
pir_sensor = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_sensor, GPIO.IN)

# Wait for the PIR sensor to settle
print("PIR sensor warming up...")
time.sleep(30)
print("PIR sensor ready")

bool openMailBox = false
bool isMail = false

# Main loop
while True:
    if GPIO.input(pir_sensor):
        print("Mailbox Opened!")
        openMailBox = True
        if(openMailBox == true){
            #We send a notification to their phone that the door has been opened.
        }
        time.sleep(60)
        if(GPIO.input(pir_sensor)){
            isMail = true
            print("You have mail delivered")
        }

    time.sleep(1)
