from fastapi import FastAPI
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}



def send_email(subject, message, to_address):
    from_address = 'luisten94@hotmail.com'
    password = os.getenv("OUTLOOK_EMAIL_PASS")  # Make sure you have this environment variable set
    msg = MIMEMultipart()
    msg['From'] = "SmartBids.ai - Email verification <" + from_address + ">"
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    # Connect to Outlook's SMTP server
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()  # Enable TLS encryption

    # Login to your Outlook account
    server.login(from_address, password)

    # Send the email
    server.sendmail(from_address, to_address, msg.as_string())

    # Close the connection
    server.quit()
