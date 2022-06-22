from smtplib import SMTP, SMTP_SSL, SMTP_SSL_PORT

class Email() :
    subject = input("Lütfen konu başlığı giriniz:")                       #Konu başlığı alır
    message = input("Lütfen mesajı giriniz:")                             #Mesaj alır
    content = ("Subject: {0} \n {1}".format(subject,message))             #Konu başlığını ve mesajı birleştirir
    
    mail = input("Lütfen email giriniz:")                                 #Gönderen email alır
    remail = input("Lütfen alıcı email giriniz:")                         #Alıcı email alır
    password = input("Lütfen şifrenizi giriniz:")                         #Gönderen email şifresi alır
    
    host = mail.split(sep = "@")                                          #Host ayarları
    host_mail = ("mail." + host)
    
    smtp_server = SMTP_SSL(host_mail, port = SMTP_SSL_PORT)
    smtp_server.set_debuglevel(1)
    smtp_server.login(mail,password)
    smtp_server.sendmail(mail,remail,password)
    