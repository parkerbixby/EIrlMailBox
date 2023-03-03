from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time
from email.message import EmailMessage
import ssl
import smtplib

pir = MotionSensor(4)

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


# Wait for the PIR sensor to settle
print("PIR sensor warming up...")
print("PIR sensor ready")

openMailBox = False

# Main loop
while True:
	pir.wait_for_motion()
	print("Mailbox Opened!")
	openMailBox = True
	if(openMailBox == True):
		with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
			smtp.login(email_sender, email_password)
			smtp.sendmail(email_sender, email_receiver, em.as_string())
		pir.wait_for_no_motion()
