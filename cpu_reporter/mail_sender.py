import smtplib
from email.mime.text import MIMEText

gmail_username = "test.bobby.demo@gmail.com"

with open("pass.txt") as f:
    gmail_pass = f.readlines()[0]

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login(gmail_username, gmail_pass)


def send_mail(msg):
    msg['Subject'] = f'CPU reporter'
    msg['From'] = gmail_username
    msg['To'] = "atanas.bozhanin@gmail.com"
    server.sendmail(gmail_username, "atanas.bozhanin@gmail.com", msg.as_string())

