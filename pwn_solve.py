from pwn import *

# context.update(arch='x86_64', bits='64')
p = process('start_dunnet')

# out = p.recv().decode('utf-8').split(': ')