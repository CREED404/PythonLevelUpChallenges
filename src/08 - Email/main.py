import smtplib
from email.message import EmailMessage

user_acc = "yourAcc@gmail.com"
acc_passwd = "yourPassword"
mail_server = "smtp.gmail.com"
mail_port = 465

def send_mail(receiver, subject, body):
  
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"]    = user_acc
    msg["To"]      = receiver
  
    with smtplib.SMTP_SSL(mail_server, mail_port) as server:
        server.login(user_acc, acc_passwd)
        server.send_message(msg)
