import subprocess
import os
import random

def generate_private_key(strength):
    tempkey = str(str(random.randint(100000000000, 999999999999)) + '.key')
    cmd = ['openssl', 'genrsa', '-out', tempkey, strength, '-passin', 'stdin']
    p = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False
    )
    out, err = p.communicate()

    f = open(tempkey, 'r')
    os.remove(tempkey)
    return f.read()


def generate_self_signed():
    pass

def verify_cert_key():
    pass

def convert_pem():
    pass

def generate_csr(*args, **kwargs):
    tempkey = str(str(random.randint(100000000000, 999999999999)) + '.key')
    cmd = ['openssl', 'genrsa', '-out', tempkey, strength, '-passin', 'stdin']
    p = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False
    )
    out, err = p.communicate()

    f = open(tempkey, 'r')
    os.remove(tempkey)
    return f.read()