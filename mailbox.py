from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time
from email.message import EmailMessage
import ssl
import smtplib

pir = MotionSensor(4)
#Setting email sender
email_sender = 'ianmyers236@gmail.com'
email_password = 'ywnoyarwjwbqsxew'
#Setting the receiver
email_receiver = 'parkerbixby01@gmail.com'

#Setting the subject for the email
subject = "Mailbox"
#The body of the email
body = "Your mailbox has been opened"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

openMailBox = False

# Main loop
while True:
	#This is checking for motion
	pir.wait_for_motion()
	print("Mailbox Opened!")
	openMailBox = True
	#If there is motion then the email will be sent to the user
	if(openMailBox == True):
		with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
			smtp.login(email_sender, email_password)
			smtp.sendmail(email_sender, email_receiver, em.as_string())
		#Now we wait till there is no motion and walk through the loop again
	pir.wait_for_no_motion()
