#sendig email through python


import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('sukhmeets111@gmail.com','rkpszjcpeivirgme')
server.sendmail('sukhmeets111@gmail.com','h4rmeet@gmail.com','python tutorial')
print("Mail sent")
server.quit()