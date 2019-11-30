from pwn import *
from time import sleep

p = process('start_dunnet')

questions = [
    'Give either of the two last names in the mailroom, other than your own.\n',
    'What cartoon character is on the towel?\n',
    'What network protocol is used between pokey and gamma?\n',
    'How many pounds did the weight weigh?\n',
    'Name the STREET which runs right over the subway stop.\n',
    'What is your login name on the \'endgame\' machine?\n',
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
    'What is your password on the machine called \'pokey\'?\n',
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
def dis(num_lines):
    for _ in range(num_lines):
        print(p.readline().decode('utf-8'), end='')
    print()
    # sleep(.1)

def write_slow(command):
    for char in command:
        print(char, end='')
        # sleep(.01)
    print()

def do(command):
    write_slow(command)
    p.sendline(command)

def q_and_a():
    q_line = p.readline().decode('utf-8')
    print(q_line)
    for i in range(len(questions)):
        if q_line == questions[i]:
            if q_line == questions[12]:
                dis(1)
            do(answers[i])

# could loop over each but dis is custom for each command
if __name__ == "__main__":
    dis(7)
    do('take all')
    dis(1)
    do('e')
    dis(4)
    do('e')
    dis(3)
    do('dig')
    dis(1)
    do('take all')
    dis(1)
    do('se')
    dis(3)
    do('take all')
    dis(1)
    do('se')
    dis(4)
    do('feed bear')
    dis(2)
    do('take all')
    dis(1)
    do('sw')
    dis(2)
    do('take all')
    dis(1)
    do('ne')
    dis(1)
    do('nw')
    dis(1)
    do('nw')
    dis(1)
    do('ne')
    dis(2)
    do('ne')
    dis(3)
    do('ne')
    dis(3)
    do('w')
    dis(7)
    do('put cpu in vax')
    dis(2)
    do('type')
    dis(4)
    do('toukmond')
    do('robert')
    dis(10)
    do('ftp gamma')
    dis(1)
    do('anonymous')
    dis(1)
    do('toukmond')
    dis(1)
    do('binary')
    dis(1)
    do('send lamp.o')
    dis(2)
    do('send shovel.o')
    dis(2)
    do('send key.o')
    dis(2)
    do('send bracelet.o')
    dis(2)
    do('quit')
    do('rlogin gamma')
    do('worms')
    dis(11)
    do('take all')
    dis(4)
    do('e')
    dis(3)
    do('n')
    dis(3)
    do('e')
    dis(6)
    do('drop shovel')
    dis(1)
    do('drop key')
    dis(1)
    do('drop bracelet')
    dis(1)
    do('take weight')
    dis(1)
    do('d')
    dis(3)
    do('drop weight')
    dis(2)
    do('nw')
    dis(2)
    do('u')
    dis(4)
    do('take all')
    dis(2)
    do('se')
    dis(2)
    do('d')
    dis(2)
    do('nw')
    dis(2)
    do('ne')
    dis(5)
    do('drop disk')
    dis(1)
    do('w')
    dis(1)
    do('s')
    dis(1)
    do('e')
    dis(4)
    do('turn dial clockwise')
    dis(1)
    do('turn dial clockwise')
    dis(1)
    do('turn dial clockwise')
    dis(3)
    do('turn dial counterclockwise')
    dis(1)
    do('w')
    dis(1)
    do('n')
    dis(1)
    do('e')
    dis(6)
    do('take all')
    dis(5)
    do('d')
    dis(2)
    do('nw')
    dis(1)
    do('u')
    dis(1)
    do('se')
    dis(1)
    do('d')
    dis(1)
    do('nw')
    dis(1)
    do('nw')
    dis(4)
    do('s')
    dis(3)
    do('s')
    dis(3)
    do('s')
    dis(2)
    do('s')
    dis(4)
    do('put bracelet in chute')
    dis(2)
    do('put diamond in chute')
    dis(2)
    do('s')
    dis(8)
    do('take all')
    dis(1)
    do('e')
    dis(3)
    do('e')
    dis(3)
    do('n')
    dis(3)
    do('d')
    dis(5)
    do('d')
    dis(3)
    do('sw')
    dis(2)
    do('e')
    dis(3)
    do('u')
    dis(3)
    do('dig')
    dis(1)
    do('take all')
    dis(1)
    do('d')
    dis(1)
    do('w')
    dis(1)
    do('w')
    dis(3)
    do('d')
    dis(3)
    do('e')
    dis(4)
    do('take all')
    dis(1)
    do('d')
    dis(2)
    do('s')
    dis(2)
    do('s')
    dis(3)
    do('s')
    dis(5)
    do('put disk in pc')
    dis(1)
    do('reset')
    dis(1)
    do('1')
    do('type foo.txt')
    dis(1)
    code = p.readline().decode('utf-8').split('is ')[1]
    print('The combination is', code, end='')
    code = code[:3] # get rid of the period
    do('exit')
    dis(3)
    do('n')
    dis(1)
    do('n')
    dis(1)
    do('n')
    dis(1)
    do('n')
    dis(2)
    do('n')
    dis(3)
    do('u')
    dis(3)
    do('put key in box')
    dis(2)
    do('u')
    dis(2)
    do('u')
    dis(3)
    do('ne')
    dis(2)
    do('ne')
    dis(4)
    do('take all')
    dis(1)
    do('d')
    dis(1)
    do('s')
    dis(3)
    do('d')
    dis(4)
    do('put gold in urinal')
    dis(1)
    do('put platinum in urinal')
    dis(1)
    do('flush')
    dis(2)
    do('n')
    dis(1)
    do('u')
    dis(1)
    do('w')
    dis(1)
    do(code)
    dis(5)
    do('cut cable')
    dis(4)
    do('exit')
    dis(6)
    do('take all')
    dis(1)
    do('e')
    dis(1)
    do('n')
    dis(6)
    do('take all')
    dis(3)
    do('w')
    dis(4)
    do('n')
    dis(7)
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

    do('n')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(2)
    do('take all')
    dis(1)
    do('e')
    dis(2)
    do('take all')
    dis(1)
    do('s')
    dis(2)
    do('take all')
    dis(1)
    do('s')
    dis(2)
    do('take all')
    dis(1)
    do('s')
    dis(2)
    do('take all')
    dis(1)
    do('e')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(2)
    do('take all')
    dis(1)
    do('e')
    dis(2)
    do('take all')
    dis(1)
    do('s')
    dis(2)
    do('take all')
    dis(1)
    do('s')
    dis(2)
    do('take all')
    dis(1)
    do('s')
    dis(2)
    do('take all')
    dis(1)
    do('e')
    dis(2)
    do('take all')
    dis(1)
    do('e')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(4) # coins here
    do('take all')
    dis(1)
    do('w')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(2)
    do('take all')
    dis(1)
    do('e')
    dis(2)
    do('take all')
    dis(1)
    do('n')
    dis(3) # bus
    do('take all')
    dis(1)
    do('w')
    dis(2)
    do('take all')
    dis(1)
    do('e')
    dis(3) # go back to normal dis (you get one off during the egg search)
    do('enter')
    dis(1)
    do('w')
    dis(3)
    do('w')
    dis(3)
    do('w')
    dis(3)
    do('w')
    dis(3)
    do('w')
    dis(3)
    do('s')
    dis(3)
    do('s')
    dis(3)
    do('s')
    dis(3)
    do('nw')
    dis(5)
    do('exit')
    dis(1)
    do('n')
    dis(5) # museum lobby
    do('e')
    dis(4)
    do('e')
    dis(4)
    do('take all')
    dis(1)
    do('n')
    dis(6)
    do('take all')
    dis(1)
    do('w')
    dis(6)
    do('take all')
    dis(2)
    do('s')
    dis(1)
    do('w')
    dis(2)
    do('s')
    dis(2)
    do('se')
    dis(1)
    do('e')
    dis(1)
    do('e')
    dis(1)
    do('e')
    dis(1)
    do('e')
    dis(1)
    do('n')
    dis(1)
    do('n')
    dis(1)
    do('put glycerine in jar')
    dis(1)
    do('put acid in jar')
    dis(1)
    do('drop jar')
    dis(6)
    do('enter')
    dis(9)
    do('n')
    dis(2)
    do('n')
    dis(3)
    do('d')
    dis(4)
    do('take all')
    dis(1)
    do('u')
    dis(1)
    do('put amethyst in garbage')
    dis(2)
    do('put ruby in garbage')
    dis(2)
    do('put silver in garbage')
    dis(2)
    do('put egg in garbage')
    dis(2)
    do('put coins in garbage')
    dis(2)
    do('u')
    dis(3)
    do('w')
    dis(1)
    do('w')
    dis(1)
    do('s')
    dis(1)
    do('w')
    dis(2)
    do('s')
    dis(2)
    do('se')
    dis(1)
    do('s')
    dis(1)
    do('e')
    dis(1)
    do('s')
    dis(1)
    do('w')
    dis(2)
    do('drop key')
    dis(1)
    do('drop license')
    dis(1)
    do('type')
    do('rlogin endgame')
    dis(17)
    do('take all')
    dis(9)
    do('n')
    dis(2)
    do('n')
    dis(4)
    q_and_a()
    dis(3)
    do('n')
    dis(3)
    q_and_a()
    dis(3)
    do('n')
    dis(3)
    q_and_a()
    dis(5)
    do('drop bracelet')
    dis(1)
    do('drop diamond')
    dis(1)
    do('drop gold')
    dis(1)
    do('drop platinum')
    dis(1)
    do('drop amethyst')
    dis(1)
    do('drop silver')
    dis(1)
    do('drop ruby')
    dis(1)
    do('n')
    dis(3)
    do('take all')
    dis(1)
    do('s')
    dis(9)
    do('drop mona')
    dis(1)
    do('s')
    dis(2)
    q_and_a()
    dis(2)
    do('s')
    dis(2)
    q_and_a()
    dis(2)
    do('s')
    dis(2)
    q_and_a()
    dis(2)
    do('s')
    dis(4)
    do('take all')
    dis(2)
    do('n')
    dis(1)
    do('n')
    dis(2)
    q_and_a()
    dis(2)
    do('n')
    dis(2)
    q_and_a()
    dis(2)
    do('n')
    dis(2)
    q_and_a()
    dis(11)
    do('drop coins')
    dis(1)
    do('drop egg')
    dis(1)
    do('quit')
    dis(5)
