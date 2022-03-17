# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:55:25 2022

@author: catal
"""

import os
import smtplib
from email.message import EmailMessage

# TODO figure out when os cant get variables
# email_address = os.environ.get("gmail_app_user")
email_address = "catalunalilith2680@gmail.com"
# email_password = os.environ.get("gmail_app_pass")
email_password = "kevxdlddhhgaruqx"

msg = EmailMessage()
msg['Subject'] = "wanna scene this weekend?"
msg["From"] = email_address
msg["To"] = email_address
msg.set_content("How about 6pm-10pm this Saterday, at Tension?")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
