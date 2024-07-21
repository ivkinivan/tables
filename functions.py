from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendEmail(recipient, html, title):
    fromaddr = 'codium@bk.ru'
    mypass = 'QsKSTjQ0A72ayHgj5LLk'
    msg = MIMEMultipart()
    msg['From'] = 'Codium IT <codium@bk.ru>'
    msg['To'] = recipient
    msg['Subject'] = title
    msg.attach(MIMEText(html, 'html'))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, recipient, text)
    server.quit()
