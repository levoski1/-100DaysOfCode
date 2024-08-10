import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host = 'smtp.gmail.com'  # Replace with your SMTP host
smtp_port = 465  # Replace with your SMTP port
smtp_user = 'johnma9857@gmail.com'  # Replace with your email address
smtp_password = 'gwkl fnob zbic zgmb'  # Replace with your email password or app-specific password

# Define email parameters
from_email = smtp_user  # Replace with your email address
to_email = 'asogwanwadimma@gmail.com'  # Replace with the recipient's email address
subject = 'Test Email Code'
body = 'This is me and Lenore testing our code. If you recieve any Email that means our code is working.'

# Create a MIME message
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

try:
    # Create an SMTP session
    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    server.login(smtp_user, smtp_password)
    print("SMTP connection successful!")

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"SMTP connection failed: {e}")
finally:
    server.quit()


