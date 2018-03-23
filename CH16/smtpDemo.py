import smtplib

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
smtpobj.sendmail('my_email_address@gmail.com', 'recipient@example.com',
                 'Subject: So long.\n Dear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpobj,quit()
