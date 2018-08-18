import subprocess

filename = 'temp.key'
numbits = str(2048)

cmd = ['openssl', 'genrsa', '-out', filename, numbits, '-passin', 'stdin']


'openssl', 'genrsa', '-out', filename, numbits, '-passin', 'stdin'

p = subprocess.Popen(cmd, shell=False,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin = subprocess.PIPE)

out = p.communicate()

f = open('temp.key','r')
message = f.read()



print(message)