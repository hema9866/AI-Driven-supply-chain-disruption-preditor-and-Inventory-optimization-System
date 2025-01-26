import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email and SMTP server details
sender_email = "your_email@gmail.com"
receiver_email = "recipient@example.com"
password = "your_email_password_or_app_password"  # If using 2FA, use an App Password
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For TLS

# Create the message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Test Email from Python"
body = "This is a test email sent from Python using SMTP!"
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection with TLS

    # Login to the server
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the server connection
    server.quit()
