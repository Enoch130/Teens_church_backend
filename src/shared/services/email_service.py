# email_service.py
from email.utils import formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from src.config import Config

class EmailService:
    def __init__(self):
        self.sender = Config.EMAIL_ADDRESS
        self.password = Config.EMAIL_APP_PASSWORD

    def send_verification_email(self, recipient: str, code: str):
        subject = "Your Verification Code"
        
        # Load HTML template and inject code
        BASE_DIR = Path(__file__).resolve().parent
        html_template = (BASE_DIR / "../utils/email_temp.html").resolve().read_text()
        html_content = html_template.replace("{{CODE}}", code)

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = formataddr(("BinByte", self.sender)) 
        message["To"] = recipient

        message.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.sender, self.password)
            server.sendmail(self.sender, recipient, message.as_string())
email_service = EmailService()