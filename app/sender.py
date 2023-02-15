import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
def send(text: str, email_receiver: str):
    try:
        f = open("user.txt", 'r')
        for i in f.readlines():
            if "@" in i:
                email_sender = i[:-1]
            else:
                email_password = i


        #email_receiver = '727danil7@gmail.com'

        subject = 'Стоимость вашей работы'

        msg = MIMEMultipart('alternative')
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "plain"))
        
        part2 = MIMEText(text, 'text')

        msg.attach(part2)

        s = smtplib.SMTP_SSL('smtp.mail.ru')
        
        s.login(email_sender, email_password)

        s.sendmail(email_sender, email_receiver, msg.as_string())
        s.quit()
        return True
    except Exception as ex:
        return ex