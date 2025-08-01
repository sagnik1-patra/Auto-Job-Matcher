import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(matches, receiver_email, sender_email, sender_password):
    if not matches:
        print("❌ No matches to send.")
        return

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "🚀 Your Matched Job Listings"

    # Format job results
    body = ""
    for job in matches:
        body += f"📌 {job['title']} at {job['company']}\n{job['summary']}\n\n"

    msg.attach(MIMEText(body, 'plain'))

    try:
        print("📤 Sending email...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
