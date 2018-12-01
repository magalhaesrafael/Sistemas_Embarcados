from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
 
fromaddr = "projetoembarcados@gmail.com"
toaddr = "eduardoons@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Teste email"
 
body = "Testando o envio de email"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "image0.pjg"
attachment = open("/home/pi/projeto_final_eduardo/python/fotos/image0.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)



filename = "image1.pjg"
attachment = open("/home/pi/projeto_final_eduardo/python/fotos/image1.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)



 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "projeto1")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()