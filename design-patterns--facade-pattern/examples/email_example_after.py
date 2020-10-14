from email.message import EmailMessage
import os
import smtplib

email_address = os.getenv("GMAIL_ADDRESS", None)
email_password = os.getenv("GMAIL_APPLICATION_PASSWORD", None)


def create_email_message(to_address, subject, plaintext, html):
    msg = EmailMessage()
    msg["From"] = email_address
    msg["To"] = to_address,
    msg["Subject"] = subject,
    msg.set_content(plaintext)
    msg.add_alternative(html, subtype="html")
    return msg


def send_message(msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(email_address, email_password)
        smtp_server.send_message(msg)

    print("Email sent successfully")


msg = create_email_message(
    from_address=email_address,
    to_address="alysivji@gmail.com",
    subject="Design Patterns",
    plain_text="Design Patterns are awesome!",
    html="<html>Design Patterns are aewesome!</html>"
)
send_message(msg)
