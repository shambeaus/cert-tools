import subprocess
import os
import uuid

def generate_private_key(strength):
    tempkey = '{}.key'.format(uuid.uuid4())
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

def verify_cert_key(cert, key):
    tempcert = '{}.cert'.format(uuid.uuid4())
    tempkey = '{}.key'.format(uuid.uuid4())

    with open('./temp/{}'.format(tempcert), "w") as f:
        f.write(cert)

    with open('./temp/{}'.format(tempkey), "w") as f:
        f.write(key)

    certcmd = ['openssl', 'x509', '-noout', '-modulus', '-in', str(tempcert) ]
    keycmd = ['openssl', 'rsa', '-noout', '-modulus', '-in', str(tempkey)]

    p = subprocess.Popen(certcmd, shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    certmd5 = subprocess.check_output(('openssl', 'md5'), stdin=p.stdout)
    os.remove('./temp/{}'.format(tempcert))

    p2 = subprocess.Popen(keycmd, shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    keymd5 = subprocess.check_output(('openssl', 'md5'), stdin=p2.stdout)
    os.remove('./temp/{}'.format(tempkey))

    if certmd5.decode('utf-8') in keymd5.decode('utf-8'):
        return True, certmd5, keymd5
    else:
        return False, certmd5, keymd5

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
