"""
Quickly add configurable parameters to your application.

Add `qconfig.json` to your `.gitignore`.
That is where your secret parameters are stored.

It's a good idea to declare all the qc params up front
so that execution is not halted while your programming
for a forgotten parameter.

Usage Example:
$ vim hello.py
import quickieconfig as qc
name = qc.param("name")
print "Hi {}".format(qc.param("name"))

$ python hello.py
QuickieConfig is lacking a parameter.
Enter a value for 'name'
> Quagmire
Hi Quagmire

$ python hello.py
Hi Quagmire
"""
import json

CONFIG_PATH = "qconfig.json"

def param(key):
    conf = _read_config()
    if key in conf:
        return conf[key]
    else:
        val = _ask_param(key)
        conf[key] = val
        with open(CONFIG_PATH, 'w') as f:
            json.dump(conf, f, indent=2, sort_keys=True)
        return val


def _read_config():
    try:
        with open(CONFIG_PATH, 'r') as f:
            try:
                return json.load(f)
            except ValueError:
                return {}
    except IOError:
        return {}


def _ask_param(key):
    print "QuickieConfig is lacking a parameter."
    print "Enter a value for '{}'".format(key)
    s = raw_input("> ")
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except:
            return s
