"""
Send the morning message.
"""

import messages
import quickieconfig as qc
from sendgrid import SendGridClient, Mail

SENDGRID_USER = qc.param("SENDGRID_USER")
SENDGRID_PASS = qc.param("SENDGRID_PASS")
FROM_EMAIL = qc.param("FROM_EMAIL")
TO_ADDR = qc.param("TARGET_EMAIL")

subject = "[sleepy] Good Morning!"
body = messages.morning_message_body()
client = SendGridClient(SENDGRID_USER, SENDGRID_PASS, raise_errors=True)
message = Mail(from_email=FROM_EMAIL, to=TO_ADDR, subject=subject, text=body)

status, msg = client.send(message)
if status != 200:
    print "status", status
    print "msg", msg
