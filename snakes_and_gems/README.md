# Snakes and Gems

This was an absolutely massive (200MBish) Python file that had 40 layers that eventually decoded to a final Python file. There were also binary bits in each layer that were encoded into Python code.

`chalsolver.py` is the solution to get the final code and `decode_binary.py` prints the final binary string that you decode to get the password.

`chalsolver.py` basically Base64 decodes all of the stages, extracts all of the bits encoded in Python, and outputs the final stage + all the bits.

I really don't know how to explain this one besides that, so I guess read the code.