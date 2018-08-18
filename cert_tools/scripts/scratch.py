import subprocess

filename = 'temp.key'
numbits = str(2048)

cmd = ['openssl', 'x509', '-noout', '-modulus', '-in', 'certificate.crt',]


p = subprocess.Popen(cmd, shell=False,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin = subprocess.PIPE)

output = subprocess.check_output(('openssl', 'md5'), stdin=p.stdout)

p.wait()



print(output)