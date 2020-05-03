import smtplib , ssl
sender_email = "pythonivanka@gmail.com"
receiver_email = "ivanka.marie@gmail.com"
message = """\
    Subject: IT IS DONE

    OMG LOG ON AND CHECK SHIT ITS HERE."""

port = 465
password = "Ivanka604"
context = ssl._create_default_https_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
server.login("pythonivanka@gmail.com", password)

server.sendmail(sender_email, receiver_email, message)
