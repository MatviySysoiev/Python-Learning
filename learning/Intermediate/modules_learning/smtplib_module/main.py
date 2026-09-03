from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(
    # Read html file
    Path("learning/Intermediate/modules_learning/smtplib_module/templates/index.html").read_text())
# change $name to Matvii and $date to tomorrow
html_content = html_template.substitute({'name': 'Matvii', 'date': 'tomorrow'})

my_email['from'] = 'Matvii <matvii@gmail.com>'
my_email['to'] = 'bestfriend@gmail.com'
my_email['subject'] = "Email with new gif"
my_email.set_content(html_content, 'html')

with open('learning/Intermediate/modules_learning/smtplib_module/images/email.gif', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image',
                            subtype='gif', filename='email.gif')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()  # Create connection with smtp server
    # smtp_server.starttls() # encryption
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")
