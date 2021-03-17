import smtplib


gmail_username = "test.bobby.demo@gmail.com"

with open("pass.txt") as f:
    gmail_pass = f.readlines()[0]

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login(gmail_username, gmail_pass)
message = """\
Subject: CPU report

{}"""


def send_mail(body: str):
    server.sendmail(gmail_username, gmail_username, message.format(body))