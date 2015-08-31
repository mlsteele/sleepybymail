from sendgrid import SendGridClient, Mail

import quickieconfig as qc

SENDGRID_USER = qc.param("SENDGRID_USER")
SENDGRID_PASS = qc.param("SENDGRID_PASS")
FROM_EMAIL = qc.param("FROM_EMAIL")
TO_ADDR = qc.param("TARGET_EMAIL")
BODY = "foo"

client = SendGridClient(SENDGRID_USER, SENDGRID_PASS, raise_errors=True)

message = Mail(from_email=FROM_EMAIL, to=TO_ADDR, subject="test", text=BODY)

status, msg = client.send(message)
print "status", status
print "msg", msg
