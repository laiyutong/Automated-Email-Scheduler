import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
import schedule  
import time  
  
# Function to send an email  
def send_email():  
    # Gmail account credentials  
    gmail_user = 'your_email@gmail.com'  
    gmail_password = 'your_password'  
      
    # Recipient email  
    to = 'recipient_email@gmail.com'  
      
    # Email content  
    subject = 'Scheduled Email'  
    body = 'This is a test email sent by a Python script!'  
      
    # Create the email message  
    msg = MIMEMultipart()  
    msg['From'] = gmail_user  
    msg['To'] = to  
    msg['Subject'] = subject  
    msg.attach(MIMEText(body, 'plain'))  
      
    # Send the email  
    try:  
        server = smtplib.SMTP('smtp.gmail.com', 587)  
        server.starttls()  
        server.login(gmail_user, gmail_password)  
        text = msg.as_string()  
        server.sendmail(gmail_user, to, text)  
        server.quit()  
        print('Email sent successfully')  
    except Exception as e:  
        print(f'Failed to send email: {e}')  
  
# Schedule the email to be sent at a specific time  
schedule.every().day.at("09:00").do(send_email)  # Send email every day at 9 AM  
  
# Keep the script running  
while True:  
    schedule.run_pending()  
    time.sleep(1)  
