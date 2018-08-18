import subprocess
import os

def generate_private_key(strength):
    cmd = ['openssl', 'genrsa', '-out', 'temp.key', strength, '-passin', 'stdin']
    p = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False
    )
    out, err = p.communicate()

    f = open('temp.key', 'r')
    os.remove('temp.key')
    return f.read()