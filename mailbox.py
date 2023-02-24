import RPi.GPIO as GPIO
import time
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'ianmyers236@gmail.com'
email_password = 'ywnoyarwjwbqsxew'

email_receiver = 'parkerbixby01@gmail.com'

subject = "Mailbox"
body = "Your mailbox has been opened"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

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
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        }
    time.sleep(1)
