from pwn import *
from time import sleep

p = process('start_dunnet')

def dis(num_lines):
    for _ in range(num_lines):
        print(p.readline().decode('utf-8'), end='')
    print()
    sleep(1)

def write_slow(command):
    for char in command:
        print(char, end='')
        sleep(.1)
    print()

def please(command):
    # print(command)
    write_slow(command)
    p.sendline(command)
    
if __name__ == "__main__":
    dis(7)
    please('take all')
    dis(1)
    please('e')
    dis(4)
    please('e')
    dis(3)

