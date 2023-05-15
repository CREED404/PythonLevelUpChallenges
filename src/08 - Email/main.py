import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, receiver, subject, body):
  email = MIMEMultipart()
  email["From"] = sender
  email["To"] = receiver
  email["Subject"] = subject

  email.attach(MIMEText(body, "plain"))

  raw = email.as_string()
  print(raw)

  try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
      server.starttls()
      server.login(sender, password)
      server.sendmail(sender, receiver, raw)
    print(f"Email sent successfully to {receiver}")
  except smtplib.SMTPException as e:
    print(e)