import smtplib

def send_email(sender, password, receiver, subject, body):
  message = f"Subject:{subject}\n\n{body}"

  with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)