import smtplib
from email.message import EmailMessage


class EmailSending:
    def __init__(self):
        self.__ownermail = "cozyspace21@gmail.com"
        self.__password = "nqxzwyzhytrcrdqb"
        self.to = 'jaikumar00.jk@gmail.com'
        self.sub = ''
        self.body = ''
        self.msg = EmailMessage()
    
    def sendMail(self):
        returnStatus = False
        try:
            self.msg['From'] =  self.__ownermail
            self.msg['To'] = self.to
            self.msg['Subject'] = self.sub
            self.msg.set_content(self.body)
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(self.__ownermail, self.__password)
                smtp.send_message(self.msg)
                returnStatus = True
        except (smtplib.SMTPException, Exception) as ERR:
            returnStatus = False
        return returnStatus