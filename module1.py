def emailsender(message, receiverEmail):
    content = message
    sender_email = "ctrcG285192044py@gmail.com"
    password = "C^rc7GU4r14n"
    receiver_email = receiverEmail
    port = 587
    smtp_server = "smtp.gmail.com"
    mail = smtplib.SMTP(smtp_server, port)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, password)
    mail.sendmail(sender_email, receiver_email, content)