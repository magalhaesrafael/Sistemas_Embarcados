#Carrega as bibliotecas para envio de e-mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

# Carrega as bibliotecas da camera, GPIO e tempo
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from time import gmtime, strftime, sleep

#Define a GPIO do sensor PIR
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

#Prepara a camera
camera = PiCamera()
camera.rotation = 180

#Definicao do email
i=0

while True:
    i=0
    estado = GPIO.input(11) #valor binario e resgistrado pelo sensor e guardado na variavel estado
    
    if estado == 0:
        time.sleep(0.1)
        
    elif estado == 1:
        #Captura das fotos
        print ("Movimento detectado");
        for i in range(2):
            sleep(2)
            camera.capture('/home/pi/Monitoramento/fotos/imagem%s.jpg' % i)
            print ("A proxima leitura sera feita em 20 segundos\n");
            time.sleep(20)
        
        #Envia o email
        fromaddr = "projetodemonitoramento@gmail.com"
        toaddr = "magalhaesrafael07@gmail.com"
 
        msg = MIMEMultipart()
 
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Registro de movimento"
         
        diaehora = strftime ("%d-%m-%Y %H:%M:%S", gmtime())
        mensagem = "Movimento detectado em:\n" + diaehora
 
        msg.attach(MIMEText(mensagem, 'plain'))
 
        filename = "imagem0.jpg"
        attachment = open("/home/pi/Monitoramento/fotos/imagem0.jpg", "rb")
 
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

        filename = "imagem1.jpg"
        attachment = open("/home/pi/Monitoramento/fotos/imagem1.jpg", "rb")
 
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "gama2018")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        