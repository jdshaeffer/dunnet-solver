# dunnet-solver
script that solves Dunnet, the beloved Emacs text adventure by Ron Schnell in the least moves possible ***with style***.

## install

for starters, you'll need the basics: `python3`, `pip3`, `emacs`

then `pwntools`: `pip3 install git+https://github.com/arthaud/python3-pwntools.git --user`

`pwntools` can be tricky to install, so follow their directions carefully.

if you have syntax error issue arise after installing on macOS, take a look here: https://github.com/arthaud/python3-pwntools/issues/3

`pwntools` does not fully support Windows, but there are some workarounds: https://github.com/masthoon/pwintools

if everything worked, run `python3 pwn_solve.py` and enjoy
