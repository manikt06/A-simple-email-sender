import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'MT'

email['to'] = '.....@gmail.com'

email['subject'] = 'recruitment'

email.set_content('You are recruited to XYZ.')
with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp1:
    smtp1.ehlo()
    smtp1.starttls()
    smtp1.login('...@gmail.com',password='...') #here choose your password after completing 2 step verification from gmail
    smtp1.send_message(email)
