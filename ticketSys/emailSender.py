# -*- coding: cp1252 -*-
## ASU Racing Team IT Department
## Automated E-mail Sender
## Created 24/9/2016
## Use Python shell
## "NOTE THIS PROGRAM SENDS ONLY EMAILS FROM GMAIL" argument1->TextFile  argument2->E-mail
##//  python Script.py emails.txt example@gmail.com  // and then enter

####NOTE "USE THE RIGHT FORMAT FOR THE E-MAILS SHEET"
##recipantName
##E-mailAddress

import getpass
import sys
import re
import os
import smtplib  ##liberary that will be used to send mails to internet machines
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ticketSys.models import Ticket

# E-mail address used for sending mails, ##'WILL BE SEEN BY THE RECIPANT'
fromAddress = 'testasurtit@gmail.com'  ##Enter a sender MAIL ADDRESS as a SECOND ARGUMENT

username = fromAddress  # User name used for logging to the Gmail server
password = 'testasurtit1'  # The password related to the username
massage = ' '  # massage will be sent by the system and will be modefied for each recipant


##A function sets up the protocole object and sends e-mailes to the server
def autoMailSender(receiver, pk, domain):
    print('email=' + receiver)
    toAddress = receiver  # E-mail address of the recipant, the example mail will be replaced by different addresses from the mailes file

    def sendEmail():
        server = smtplib.SMTP('smtp.gmail.com:587')  # Using Gmail
        server.ehlo()  # Our System's object and the server shaking hand
        server.starttls()  # Something to do with encryption
        server.login(username, password)  # Logging to the server
        server.sendmail(fromAddress, toAddress, massage)  # Sending e-mail using the information above
        server.quit()  # Stop Communication with the server

    try:
        msg = MIMEMultipart('alternative')  # Choose alternative for the mail extension to mix between html and text
        msg[
            'Subject'] = "FSUK'17 job vacancy application"  # Set the Subject this method will set it automaticaly to the header
        msg['From'] = 'HR Department ASURT'  # The From attribute will show in the lable of the E-mail
        msg['To'] = toAddress  # The To attribute will appear to the recipant

        # Creating the TEXT and the HTML part of the massage
        text = "Hi this is an Automated mail from ASURT send to"

        ticket = Ticket.objects.get(id=pk)
        url = domain + ticket.get_absolute_url()
        html = """
        <html>
          <head></head>
          <body>
            <p>
               check the ticket System<br><br>
                %s <br><br>
               Best regards,<br>
               HR-Department,<br>
               ASU Racing Team.<br>
            </p>
          </body>
        </html>
        """ % (url)
        # Define the type of each part
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        massage = msg.as_string()
        # FINISH Creating massage to send
        sendEmail()

    except smtplib.SMTPException:
        print("---ERROR---Has not been sent", toAddress)
        print(
            "Error: unable to send email ,\n try Access for less secure apps \nfor GMAIL go to:\nhttps://www.google.com/settings/security/lesssecureapps")
        sys.exit("Error")
