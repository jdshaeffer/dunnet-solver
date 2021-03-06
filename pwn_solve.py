from pwn import *
from time import sleep

questions = [
    'Give either of the two last names in the mailroom, other than your own.\n',
    'What cartoon character is on the towel?\n',
    'What network protocol is used between pokey and gamma?\n',
    'How many pounds did the weight weigh?\n',
    'Name the STREET which runs right over the subway stop.\n',
    'What is your login name on the ‘endgame’ machine?\n',
    'How many corners are there in town (excluding the one with the Post Office)?\n',
    'What password did you use during anonymous ftp to gamma?\n',
    'What is the nearest whole dollar to the price of the shovel?\n',
    'Name either of the two objects you found by digging.\n',
    'What type of bear was hiding your key?\n',
    'How many megabytes of memory is on the CPU board for the Vax?\n',
    'Excluding the endgame, how many places are there where you can put\n', # 2 line question
    'What is the last name of the author of EMACS?\n',
    'What is the name of the bus company serving the town?\n',
    'Which street in town is named after a U.S. state?\n',
    'What is your password on the machine called ‘pokey’?\n',
]

# question 0 is answer 0
answers = [
    'answer stock',
    'answer snoopy',
    'answer tcp',
    'answer 10',
    'answer fourth',
    'answer toukmond',
    'answer 24',
    'answer toukmond',
    'answer 20',
    'answer cpu',
    'answer grizzly',
    'answer 2',
    'answer 4',
    'answer stallman',
    'answer mobytours',
    'answer Vermont',
    'answer robert'
]

# needs to be exact number of lines displayed
def dis(p, num_lines, speed):
    for _ in range(num_lines):
        print(p.readline().decode('utf-8'), end='')
    print()
    sleep(speed) # .1

def write_slow(p, command, speed):
    for char in command:
        print(char, end='')
        sleep(speed / 10) # .01
    print()

def do(p, command, speed):
    write_slow(p, command, speed)
    p.sendline(command)

def q_and_a(p, speed):
    q_line = p.readline().decode('utf-8')
    print(q_line)
    for i in range(len(questions)):
        if q_line == questions[i]:
            if q_line == questions[12]:
                dis(p, 1, speed)
            do(p, answers[i], speed)

def welcome():
    print('''
 _____     __  __     __   __     __   __     ______     ______  
/\  __-.  /\ \/\ \   /\ "-.\ \   /\ "-.\ \   /\  ___\   /\__  _\ 
\ \ \/\ \ \ \ \_\ \  \ \ \-.  \  \ \ \-.  \  \ \  __\   \/_/\ \/ 
 \ \____-  \ \_____\  \ \_\\\\"\_\  \ \_\\\\"\_\  \ \_____\    \ \_\ 
  \/____/   \/_____/   \/_/ \/_/   \/_/ \/_/   \/_____/     \/_/ 
    ''')
    print('''
 ______     ______     __         __   __   ______     ______    
/\  ___\   /\  __ \   /\ \       /\ \ / /  /\  ___\   /\  == \   
\ \___  \  \ \ \/\ \  \ \ \____  \ \ \\'/   \ \  __\   \ \  __<   
 \/\_____\  \ \_____\  \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ 
  \/_____/   \/_____/   \/_____/   \/_/      \/_____/   \/_/ /_/ 
    ''')
    print('note: dunnet 2.01 was written by Ron Schnell, I hold no rights to his game.\n')
    print('how fast do you want to solve dunnet? (slow, medium, quick, blazin, justdoit)')
    chosen = False
    while not chosen:
        x = input('> ')
        if x == 'slow':
            speed = 2.1
            chosen = True
        elif x == 'medium':
            speed = 1.1
            chosen = True
        elif x == 'quick':
            speed = .5
            chosen = True
        elif x == 'blazin':
            speed = .1
            chosen = True
        elif x == 'justdoit':
            speed = 0
            chosen = True
        else:
            print('I didn\'t understand that')
        
    return speed

# could loop over each but dis is custom for each command
def main(speed):
    p = process('dunnet.sh')
    dis(p, 7, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 4, speed)
    do(p, 'e', speed)
    dis(p, 3, speed)
    do(p, 'dig', speed)
    dis(p, 1, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'se', speed)
    dis(p, 3, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'se', speed)
    dis(p, 4, speed)
    do(p, 'feed bear', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'sw', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'ne', speed)
    dis(p, 1, speed)
    do(p, 'nw', speed)
    dis(p, 1, speed)
    do(p, 'nw', speed)
    dis(p, 1, speed)
    do(p, 'ne', speed)
    dis(p, 2, speed)
    do(p, 'ne', speed)
    dis(p, 3, speed)
    do(p, 'ne', speed)
    dis(p, 3, speed)
    do(p, 'w', speed)
    dis(p, 7, speed)
    do(p, 'put cpu in vax', speed)
    dis(p, 2, speed)
    do(p, 'type', speed)
    dis(p, 4, speed)
    do(p, 'toukmond', speed)
    do(p, 'robert', speed)
    dis(p, 10, speed)
    do(p, 'ftp gamma', speed)
    dis(p, 1, speed)
    do(p, 'anonymous', speed)
    dis(p, 1, speed)
    do(p, 'toukmond', speed)
    dis(p, 1, speed)
    do(p, 'binary', speed)
    dis(p, 1, speed)
    do(p, 'send lamp.o', speed)
    dis(p, 2, speed)
    do(p, 'send shovel.o', speed)
    dis(p, 2, speed)
    do(p, 'send key.o', speed)
    dis(p, 2, speed)
    do(p, 'send bracelet.o', speed)
    dis(p, 2, speed)
    do(p, 'quit', speed)
    do(p, 'rlogin gamma', speed)
    do(p, 'worms', speed)
    dis(p, 11, speed)
    do(p, 'take all', speed)
    dis(p, 4, speed)
    do(p, 'e', speed)
    dis(p, 3, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    do(p, 'e', speed)
    dis(p, 6, speed)
    do(p, 'drop shovel', speed)
    dis(p, 1, speed)
    do(p, 'drop key', speed)
    dis(p, 1, speed)
    do(p, 'drop bracelet', speed)
    dis(p, 1, speed)
    do(p, 'take weight', speed)
    dis(p, 1, speed)
    do(p, 'd', speed)
    dis(p, 3, speed)
    do(p, 'drop weight', speed)
    dis(p, 2, speed)
    do(p, 'nw', speed)
    dis(p, 2, speed)
    do(p, 'u', speed)
    dis(p, 4, speed)
    do(p, 'take all', speed)
    dis(p, 2, speed)
    do(p, 'se', speed)
    dis(p, 2, speed)
    do(p, 'd', speed)
    dis(p, 2, speed)
    do(p, 'nw', speed)
    dis(p, 2, speed)
    do(p, 'ne', speed)
    dis(p, 5, speed)
    do(p, 'drop disk', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 4, speed)
    do(p, 'turn dial clockwise', speed)
    dis(p, 1, speed)
    do(p, 'turn dial clockwise', speed)
    dis(p, 1, speed)
    do(p, 'turn dial clockwise', speed)
    dis(p, 3, speed)
    do(p, 'turn dial counterclockwise', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 6, speed)
    do(p, 'take all', speed)
    dis(p, 5, speed)
    do(p, 'd', speed)
    dis(p, 2, speed)
    do(p, 'nw', speed)
    dis(p, 1, speed)
    do(p, 'u', speed)
    dis(p, 1, speed)
    do(p, 'se', speed)
    dis(p, 1, speed)
    do(p, 'd', speed)
    dis(p, 1, speed)
    do(p, 'nw', speed)
    dis(p, 1, speed)
    do(p, 'nw', speed)
    dis(p, 4, speed)
    do(p, 's', speed)
    dis(p, 3, speed)
    do(p, 's', speed)
    dis(p, 3, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 4, speed)
    do(p, 'put bracelet in chute', speed)
    dis(p, 2, speed)
    do(p, 'put diamond in chute', speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 8, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 3, speed)
    do(p, 'e', speed)
    dis(p, 3, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    do(p, 'd', speed)
    dis(p, 5, speed)
    do(p, 'd', speed)
    dis(p, 3, speed)
    do(p, 'sw', speed)
    dis(p, 2, speed)
    do(p, 'e', speed)
    dis(p, 3, speed)
    do(p, 'u', speed)
    dis(p, 3, speed)
    do(p, 'dig', speed)
    dis(p, 1, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'd', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 3, speed)
    do(p, 'd', speed)
    dis(p, 3, speed)
    do(p, 'e', speed)
    dis(p, 4, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'd', speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 3, speed)
    do(p, 's', speed)
    dis(p, 5, speed)
    do(p, 'put disk in pc', speed)
    dis(p, 1, speed)
    do(p, 'reset', speed)
    dis(p, 1, speed)
    do(p, '1', speed)
    do(p, 'type foo.txt', speed)
    dis(p, 1, speed)
    code = p.readline().decode('utf-8').split('is ')[1]
    print('The combination is', code, end='')
    code = code[:3] # get rid of the period
    do(p, 'exit', speed)
    dis(p, 3, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    do(p, 'u', speed)
    dis(p, 3, speed)
    do(p, 'put key in box', speed)
    dis(p, 2, speed)
    do(p, 'u', speed)
    dis(p, 2, speed)
    do(p, 'u', speed)
    dis(p, 3, speed)
    do(p, 'ne', speed)
    dis(p, 2, speed)
    do(p, 'ne', speed)
    dis(p, 4, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'd', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 3, speed)
    do(p, 'd', speed)
    dis(p, 4, speed)
    do(p, 'put gold in urinal', speed)
    dis(p, 1, speed)
    do(p, 'put platinum in urinal', speed)
    dis(p, 1, speed)
    do(p, 'flush', speed)
    dis(p, 2, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'u', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 1, speed)
    do(p, code, speed)
    dis(p, 5, speed)
    do(p, 'cut cable', speed)
    dis(p, 4, speed)
    do(p, 'exit', speed)
    dis(p, 6, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 6, speed)
    do(p, 'take all', speed)
    dis(p, 3, speed)
    do(p, 'w', speed)
    dis(p, 4, speed)
    do(p, 'n', speed)
    dis(p, 7, speed)
    
    # the problem is if you read too many lines than what are available, it freezes
    # if there's more to be read, then do so
    # egg_check = p.readline().decode('utf-8')
    # if egg_check == 'There is a jewel-encrusted egg here.':
    #     print(egg_check)
    #     do('take all')
    #     dis(1)
    # else:
    #     do('n')
    #     print(egg_check)
    #     dis(1)

    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 4, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 2, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 3, speed) # go back to normal dis (you get one off during the egg search)
    do(p, 'enter', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 3, speed)
    do(p, 'w', speed)
    dis(p, 3, speed)
    do(p, 'w', speed)
    dis(p, 3, speed)
    do(p, 'w', speed)
    dis(p, 3, speed)
    do(p, 'w', speed)
    dis(p, 3, speed)
    do(p, 's', speed)
    dis(p, 3, speed)
    do(p, 's', speed)
    dis(p, 3, speed)
    do(p, 's', speed)
    dis(p, 3, speed)
    do(p, 'nw', speed)
    dis(p, 5, speed)
    do(p, 'exit', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 5, speed)
    do(p, 'e', speed)
    dis(p, 4, speed)
    do(p, 'e', speed)
    dis(p, 4, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 6, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 6, speed)
    do(p, 'take all', speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'se', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'put glycerine in jar', speed)
    dis(p, 1, speed)
    do(p, 'put acid in jar', speed)
    dis(p, 1, speed)
    do(p, 'drop jar', speed)
    dis(p, 6, speed)
    do(p, 'enter', speed)
    dis(p, 9, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    do(p, 'd', speed)
    dis(p, 4, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 'u', speed)
    dis(p, 1, speed)
    do(p, 'put amethyst in garbage', speed)
    dis(p, 2, speed)
    do(p, 'put ruby in garbage', speed)
    dis(p, 2, speed)
    do(p, 'put silver in garbage', speed)
    dis(p, 2, speed)
    do(p, 'put egg in garbage', speed)
    dis(p, 2, speed)
    do(p, 'put coins in garbage', speed)
    dis(p, 2, speed)
    do(p, 'u', speed)
    dis(p, 3, speed)
    do(p, 'w', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    do(p, 'se', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 1, speed)
    do(p, 'e', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 1, speed)
    do(p, 'w', speed)
    dis(p, 2, speed)
    do(p, 'drop key', speed)
    dis(p, 1, speed)
    do(p, 'drop license', speed)
    dis(p, 1, speed)
    do(p, 'type', speed)
    do(p, 'rlogin endgame', speed)
    dis(p, 17, speed)
    do(p, 'take all', speed)
    dis(p, 9, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    do(p, 'n', speed)
    dis(p, 4, speed)
    q_and_a(p, speed)
    dis(p, 3, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    q_and_a(p, speed)
    dis(p, 3, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    q_and_a(p, speed)
    dis(p, 5, speed)
    do(p, 'drop bracelet', speed)
    dis(p, 1, speed)
    do(p, 'drop diamond', speed)
    dis(p, 1, speed)
    do(p, 'drop gold', speed)
    dis(p, 1, speed)
    do(p, 'drop platinum', speed)
    dis(p, 1, speed)
    do(p, 'drop amethyst', speed)
    dis(p, 1, speed)
    do(p, 'drop silver', speed)
    dis(p, 1, speed)
    do(p, 'drop ruby', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 3, speed)
    do(p, 'take all', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 9, speed)
    do(p, 'drop mona', speed)
    dis(p, 1, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    q_and_a(p, speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    q_and_a(p, speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 2, speed)
    q_and_a(p, speed)
    dis(p, 2, speed)
    do(p, 's', speed)
    dis(p, 4, speed)
    do(p, 'take all', speed)
    dis(p, 2, speed)
    do(p, 'n', speed)
    dis(p, 1, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    q_and_a(p, speed)
    dis(p, 2, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    q_and_a(p, speed)
    dis(p, 2, speed)
    do(p, 'n', speed)
    dis(p, 2, speed)
    q_and_a(p, speed)
    dis(p, 11, speed)
    do(p, 'drop coins', speed)
    dis(p, 1, speed)
    do(p, 'drop egg', speed)
    dis(p, 1, speed)
    do(p, 'quit', speed)
    dis(p, 5, speed)

if __name__ == "__main__":
    yes = ['yes','ye','y','yeet','yep','yeah']
    while 1:
        speed = welcome()
        main(speed)
        sleep(2)
        print('\nawesome job dooder')
        print('care to try again?')
        if input('> ') not in yes:
            print('okay, have a gud day\n')
            break;
