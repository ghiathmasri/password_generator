import string
import random
import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage:\n{0} <passwordlength>".format(sys.argv[0]))
    exit(1)


length = int(sys.argv[1])


def genPassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size = length
    return ''.join(random.choice(chars) for x in range(size))

password = genPassword()
subprocess.run("pbcopy", universal_newlines=True, input=password)

print("Password is saved to your clipboard")