import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sendmail():
    fromaddres = "sergeyveletnyuk@mail.ru"
    toaddr = "sergeyveletnyuk@mail.ru"
    mypass = "iSj09Ni7MfaXreYaPye8"
    reportname = "log.txt"

    msg = MIMEMultipart()
    msg['From'] = fromaddres
    msg['To'] = toaddr
    msg['Subject'] = "Привет от питона"

    with open(reportname, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
        msg.attach(part)
    #
    body = "Это пробное сообщение"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

    # server.starttls()
    server.login(fromaddres, mypass)
    text = msg.as_string()
    server.sendmail(fromaddres, toaddr, text)
    server.quit()

