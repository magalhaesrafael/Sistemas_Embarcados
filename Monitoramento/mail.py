import smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText

msg = MIMEMultipart()

senha = "gama2018"
msg['From'] = "projetodemonitoramento@gmail.com"
msg['To'] = "magalhaesrafael07@gmail.com"
msg['Subject'] = "Sistema de Monitoramento"

msg.attach(MIMEImage(file('/home/pi/Monitoramento/imagem0.jpg'.read())))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], senha)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print ("Email enviado com sucesso para %s:" %(msg['To']))
