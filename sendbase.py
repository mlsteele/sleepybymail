"""
Base code for sending a message.
"""

import quickieconfig as qc
from sendgrid import SendGridClient, Mail

SENDGRID_USER = qc.param("SENDGRID_USER")
SENDGRID_PASS = qc.param("SENDGRID_PASS")
FROM_EMAIL = qc.param("FROM_EMAIL")
TO_ADDR = qc.param("TARGET_EMAIL")

def send_email(subject, body):
    """Send a message with stuff filled in for sleepybymail."""
    client = SendGridClient(SENDGRID_USER, SENDGRID_PASS, raise_errors=True)
    message = Mail(
            from_email=FROM_EMAIL,
            to=TO_ADDR,
            subject=subject,
            html=body,
            text=body)

    status, msg = client.send(message)

    if status != 200:
        print "status", status
        print "msg", msg
