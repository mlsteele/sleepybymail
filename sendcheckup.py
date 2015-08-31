"""
Send the checkup message.
"""

import sendbase
import messages

if __name__ == "__main__":
    subject = "[sleepy] Just checking in on you."
    body = messages.checkup_message_body()
    sendbase.send_email(subject, body)
