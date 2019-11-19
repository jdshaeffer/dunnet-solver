import subprocess
from time import sleep

def out(output):
    print(output.decode('utf-8'))

def write(p, command):
    p.stdin.write(command.encode('utf-8'))
    sleep(1)

dunnet = 'emacs -batch -l dunnet'

p = subprocess.Popen(dunnet.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
write(p, 'help')
output, error = p.communicate()
out(output)


