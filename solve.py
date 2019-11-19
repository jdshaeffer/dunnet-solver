from subprocess import Popen, PIPE
from time import sleep

# def out(output):
#     print(output.decode('utf-8'))

# def write(p, command):
#     p.stdin.write(command.encode('utf-8'))
#     p.stdin.flush()

dunnet = 'emacs -batch -l dunnet'

p = Popen(dunnet.split(), stdout=PIPE, stdin=PIPE)
out = p.communicate(input=b'take all\nhello')[0]
print(out.decode('utf-8'))

