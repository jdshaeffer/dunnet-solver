# from subprocess import Popen, PIPE
# from time import sleep

# def out(output):
#     print(output.decode('utf-8'))

# def write(p, command):
#     p.stdin.write(command.encode('utf-8'))
#     p.stdin.flush()

import subprocess

dunnet = './dunnet.sh'

with open('dunnet_fkt.txt', 'rb', 0) as input_file:
    subprocess.check_call(dunnet, stdin=input_file)

# p = Popen(dunnet.split(), stdout=PIPE, stdin=PIPE)
# take_all = p.communicate(input=b'take all')[0]
# input(">>")
# print(take_all.decode('utf-8'))
# help = p.communicate(input=b'help')[0]
# input(">>")
# print(help.decode('utf-8'))
