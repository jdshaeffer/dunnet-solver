# dunnet-solver
script that solves dunnet 2.01, the beloved Emacs text adventure by Ron Schnell in the least moves possible ***with style***.

## install

for starters, you'll need the basics: `python3`, `pip3`, `emacs`

then `pwntools`: `pip3 install git+https://github.com/arthaud/python3-pwntools.git --user`

`pwntools` can be tricky to install, so follow their directions carefully

if you run into any issues, feel free to submit an issue and I'll help you out

on macOS, a common error you might see when installing `pwntools` is a syntax error issue - take a look here to solve: https://github.com/arthaud/python3-pwntools/issues/3

`pwntools` does not fully support Windows, but there are some workarounds: https://github.com/masthoon/pwintools

if everything worked, run `python3 pwn_solve.py` and enjoy

## a few notes

- I solved Dunnet personally with very few hints and no complete walkthrough
- the sequence and order of commands is entirely my own strategy and could certainly be improved on (pr's welcome!)
- I know `get` has less characters than `take`, but `take` just sounds better to me, and doesn't affect number of commands, so the solver uses `take` for inventory pick ups.
