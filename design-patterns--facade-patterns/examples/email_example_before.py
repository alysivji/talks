from email.message import EmailMessage
import os
import smtplib

email_address = os.getenv('GMAIL_ADDRESS', None)
email_password = os.getenv('GMAIL_APPLICATION_PASSWORD', None)

msg = EmailMessage()
msg['From'] = "alysivji@gmail.com"
msg['To'] = "alysivji+test@gmail.com"
msg['Subject'] = "Design Patterns"
msg.set_content("Design Patterns are awesome!")
msg.add_alternative("<html>Design Patterns are awesome!</html>", subtype='html')

with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(email_address, email_password)
    smtp_server.send_message(msg)

print('Email sent successfully')
