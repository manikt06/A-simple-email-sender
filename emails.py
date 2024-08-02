import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'manik Tyagi'

email['to'] = 'maniktyagi1000@gmail.com'

email['subject'] = 'recruitment'

email.set_content('You are recruited to XYZ.')
with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp1:
    smtp1.ehlo()
    smtp1.starttls()
    smtp1.login('maniktyagi100@gmail.com',password='zpxn dpqp znch vbyr')
    smtp1.send_message(email)