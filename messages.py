"""
Get text for messages.
"""

import datetime
import urllib
import uuid
import quickieconfig as qc

LOG_SERVER_HOST = qc.param("LOG_SERVER_HOST")
LOG_SERVER_PORT = qc.param("LOG_SERVER_PORT")

def make_link(data):
    """Create a logging link from a simple dictionary of stuff."""
    querystring = urllib.urlencode(data)
    return "http://{}:{}/log?{}".format(
            LOG_SERVER_HOST,
            LOG_SERVER_PORT,
            querystring)

def morning_message_body():
    """Get the body text of the morning message."""
    message_uuid = uuid.uuid4()
    lines = []
    lines.append("Hello,")
    lines.append("")
    lines.append("How many hours of sleep did you get last night?")
    for n in xrange(4, 12):
        lines.append("")
        lines.append("")
        link_uuid = uuid.uuid4()
        link_href = make_link({
            "type": "automail",
            "message_uuid": message_uuid,
            "link_uuid": link_uuid,
            "time_requested": datetime.datetime.now(),
            "field": "hours_slept",
            "value": n,
            })
        lines.append("<a href=\"{}\">{}</a>".format(
            link_href,
            n))
    return "\n".join(lines)


def checkup_message_body():
    """Get the body text of the checkup message."""
    message_uuid = uuid.uuid4()
    lines = []
    lines.append("Hey there,")
    lines.append("")
    lines.append("Rate your awakeness on a scale from 1 to 5 please.")
    lines.append("")
    for n in xrange(1, 6):
        lines.append("  ")
        link_uuid = uuid.uuid4()
        link_href = make_link({
            "type": "automail",
            "message_uuid": message_uuid,
            "link_uuid": link_uuid,
            "time_requested": datetime.datetime.now(),
            "field": "awakeness",
            "value": n,
            })
        lines.append("<a href=\"{}\">{}</a>".format(
            link_href,
            n))
    return "\n".join(lines)


if __name__ == "__main__":
    print morning_message_body()
    print make_link({"type": "testing", "greeting": "yo"})
