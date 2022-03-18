# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:55:25 2022

@author: catal
"""

import os
import smtplib
import imghdr
from email.message import EmailMessage

email_address = os.environ.get("gmail_app_user")
email_password = os.environ.get("gmail_app_pass")

msg = EmailMessage()
msg['Subject'] = "wanna scene this weekend?"
msg["From"] = email_address
msg["To"] = email_address
msg.set_content("How about 6pm-10pm this Saterday, at Tension? I'll throw in some extra pussy pics ;)")

pics = ["max2DaysOld.jpg", "max3DaysOld.jpg"]
for pic in pics:
    with open(pic, "rb") as f:
        f_data = f.read()
        f_type = imghdr.what(f.name)
        f_name = f.name
    msg.add_attachment(f_data, maintype='image', subtype=f_type, filename=f_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
