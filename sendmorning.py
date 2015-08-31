"""
Send the morning message.
"""

import sendbase
import messages

if __name__ == "__main__":
    subject = "[sleepy] Good Morning!"
    body = messages.morning_message_body()
    sendbase.send_email(subject, body)
