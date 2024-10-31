# alert_manager.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD

class AlertManager:
    @staticmethod
    def send_alert(user_email, breach_info):
        """
        Sends an alert email to the user if their email is found in a data breach.

        Args:
            user_email (str): The user's email address to send the alert to.
            breach_info (list): A list of breach details found for the user's email.
        """
        # Email content
        subject = "⚠️ Dark Web Breach Alert: Your Email Was Found in Data Breaches"
        body = f"Dear user,\n\nYour email {user_email} was found in the following breaches:\n\n"
        for breach in breach_info:
            body += f"- {breach['Name']}: {breach['Description']}\n"
        body += "\nPlease take appropriate steps to secure your accounts.\n\nBest regards,\nDark Web Monitoring Team"

        # Create email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = user_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            # Sending email via SMTP server
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, user_email, msg.as_string())
            print(f"Alert email sent to {user_email}")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
